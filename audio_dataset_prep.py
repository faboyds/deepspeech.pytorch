from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
from random import seed
from random import random
# seed random number generator
seed(1)

transcript_path = '/content/drive/My Drive/emguka_dataset/Transcripts'
file_train = open("data/emguka_train_manifest_3.csv", "w")
file_val = open("data/emguka_val_manifest_3.csv", "w")

local_path = '/Users/fabiolourenco/Projects/deepspeech.pytorch/emguka_dataset/'


def iterate_dir(path):
    for f in listdir(path):
        if isfile(join(path, f)):
            if f.endswith('.wav'):
                sound = AudioSegment.from_file(join(path, f), format="wav")
                peak_amplitude = sound.max
                if peak_amplitude > 10000:
                    print(join('/content/drive/My Drive/emguka_dataset/', join(path, f).replace(local_path, '')),
                          transcript_path + '/' + join(path.replace('/audio', ''), f.replace('a_', 'transcript_').replace('wav', 'txt')).replace(local_path, ''))

                    if random() > 0.2:
                        file_train.write(join('/content/drive/My Drive/emguka_dataset/', join(path, f).replace(local_path, '')) + ',' +
                          transcript_path + '/' + join(path.replace('/audio', ''), f.replace('a_', 'transcript_').replace('wav', 'txt')).replace(local_path, '') + '\n')
                    else:
                        file_val.write(join('/content/drive/My Drive/emguka_dataset/', join(path, f).replace(local_path, '')) + ',' +
                          transcript_path + '/' + join(path.replace('/audio', ''), f.replace('a_', 'transcript_').replace('wav', 'txt')).replace(local_path, '') + '\n')
        else:
            iterate_dir(path + '/' + f)


def main():
    audio_path = '/Users/fabiolourenco/Projects/deepspeech.pytorch/emguka_dataset/audio'
    iterate_dir(audio_path)
    file_train.close()
    file_val.close()


if __name__ == "__main__":
    main()