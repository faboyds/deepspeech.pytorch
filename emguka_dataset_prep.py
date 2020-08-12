from os import listdir
from os.path import isfile, join
from random import seed
from random import random
# seed random number generator
seed(1)

transcript_path = '/content/drive/My Drive/emguka_dataset/Transcripts'
emg_path = '/content/drive/My Drive/emguka_dataset/emg'
file_train_audible = open("data/emguka_train_manifest_emg_audible.csv", "w")
file_train_silent = open("data/emguka_train_manifest_emg_silent.csv", "w")
file_train_whispered = open("data/emguka_train_manifest_emg_whispered.csv", "w")
file_val_audible = open("data/emguka_val_manifest_emg_audible.csv", "w")
file_val_silent = open("data/emguka_val_manifest_emg_silent.csv", "w")
file_val_whispered = open("data/emguka_val_manifest_emg_whispered.csv", "w")

local_path = '/Users/fabiolourenco/Projects/ssr_deepspeech.pytorch/emguka_dataset'


def iterate_dir(path):
    for f in listdir(path):
        if isfile(join(path, f)):
            with open(join(path, f), 'rb') as file:
                line = file.readline()
                while line:
                    split = [x for x in line.decode('utf8').split(':')[1].split(' ') if x.strip()]

                    if split:
                        for utterance in split:
                            session = [a.strip() for a in utterance.replace('emg_', '').split('-')]

                            entry = emg_path + '/' + session[0] + '/' + session[1] + '/' + 'e07_' + session[0] + '_' + session[1] + '_' + session[2] + '.adc' + ',' +  \
                                    transcript_path + '/' + session[0] + '/' + session[1] + '/' + 'transcript_' + session[0] + '_' + session[1] + '_' + session[2] + '.txt' + '\n'
                            print(entry)

                            if f.endswith('audible'):
                                if f.startswith('train'):
                                    file_train_audible.write(entry)
                                else:
                                    file_val_audible.write(entry)
                            if f.endswith('silent'):
                                if f.startswith('train'):
                                    file_train_silent.write(entry)
                                else:
                                    file_val_silent.write(entry)
                            if f.endswith('whispered'):
                                if f.startswith('train'):
                                    file_train_whispered.write(entry)
                                else:
                                    file_val_whispered.write(entry)

                    line = file.readline()


def main():
    subsets_file_path = '/Users/fabiolourenco/Projects/ssr_deepspeech.pytorch/emguka_dataset/Subsets'
    iterate_dir(subsets_file_path)
    file_train_audible.close()
    file_train_silent.close()
    file_train_whispered.close()
    file_val_audible.close()
    file_val_silent.close()
    file_val_whispered.close()


if __name__ == "__main__":
    main()