from os import listdir
from os.path import isfile, join
from random import seed
from random import random
# seed random number generator
seed(1)

transcript_path = '/content/drive/My Drive/emguka_dataset/Transcripts'
file_train = open("data/emguka_train_manifest_emg_1.csv", "w")
file_val = open("data/emguka_val_manifest_emg_1.csv", "w")

local_path = '/Users/fabiolourenco/Projects/ssr_deepspeech.pytorch/emguka_dataset'


def iterate_dir(path):
    for f in listdir(path):
        if isfile(join(path, f)):
            if f.endswith('.adc'):
                line = '/content/drive/My Drive/emguka_dataset' + join(path, f).replace(local_path, '') + ',' + \
                       transcript_path + join(path.replace('/emg/', '/'), f.replace('e07_', 'transcript_').replace('adc', 'txt')).replace(local_path, '')
                print(line)

                if random() > 0.2:
                    file_train.write(line + '\n')
                else:
                    file_val.write(line + '\n')
        else:
            iterate_dir(path + '/' + f)


def main():
    audio_path = '/Users/fabiolourenco/Projects/ssr_deepspeech.pytorch/emguka_dataset/emg'
    iterate_dir(audio_path)
    file_train.close()
    file_val.close()


if __name__ == "__main__":
    main()