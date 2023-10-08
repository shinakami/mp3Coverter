import os
from pydub import AudioSegment

os.system("cls")

def wav2mp3(filepath, savepath):
    sourcefile = AudioSegment.from_wav(filepath)
    filename = filepath.split('/')[-1].split('.wav')[0] + '.mp3'
    print(filename)
    sourcefile.export(savepath + filename, format="mp3")

def getFileName(filepath):
    file_list = []
    for root,dirs,files in os.walk(filepath):
        for filespath in files:
            if 'wav' in filespath.split('.')[-1]:
                file_list.append(os.path.join(root,filespath))
    return file_list

if __name__ == '__main__':
    folder = 'C:/Users/User/Desktop/戰乙女OST/戰乙女專輯DLC/'
    savepath = 'C:/Users/User/Desktop/戰乙女OST/戰乙女專輯DLC/MP3_file/'
    wav_list = getFileName(folder)
    for item in wav_list:
        wav2mp3(item, savepath)




