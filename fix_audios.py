from os import listdir, system
from os.path import isfile, join


def iterate_dir(path):
    for f in listdir(path):
        if isfile(join(path, f)):
            if f.endswith('.wav'):
                system('sox ' + path + '/' + f + ' out.wav remix 1')
                system('rm ' + path + '/' + f)
                system('cp out.wav ' + path + '/' + f)
                system('rm out.wav')
        else:
            iterate_dir(path + '/' + f)


def main():
    audio_path = '/Users/fabiolourenco/Projects/deepspeech.pytorch/emguka_dataset/audio'
    iterate_dir(audio_path)


if __name__ == "__main__":
    main()
