from scipy.misc import toimage
import matplotlib.pyplot as plt
import stft
import os
import numpy as np


# 파일 하나만 바꿔줌
def convert_one_file_to_image(file):
    x = np.loadtxt(file, delimiter=',')
    # toimage(x).show()
    toimage(x).save('all(grayscale).jpg')


# 파일 하나만 스펙트럼 이미지로 바꿔줌
def convert_one_file_to_spectrum(file):
    x = np.loadtxt(file, delimiter=',', unpack=True)
    # toimage(x).show()
    z_data = np.transpose(x[2])
    specgram_z = stft.spectrogram(z_data, window=0.4)
    plt._imsave('all(test).jpg', abs(specgram_z), vmin=-40, vmax=40, cmap=plt.get_cmap('coolwarm'), format='jpg')


# 디렉토리 내의 파일들을 한번에 일괄 변환 와 개쩐다 난 노가다했는데 ㅅㅂ 진작에 할걸
def convert_all_file_to_directory(path):

    dirs = os.listdir(path)

    for item in dirs:
        if os.path.isfile(path+item):
            print(path+item)
            x = np.loadtxt(path+item, delimiter=',')
            f, e = os.path.splitext(path+item)
            toimage(x).save(f + '.jpg')


# 스펙트럼 이미지로 일괄 변환
def convert_all_file_to_spectrum(path):

    dirs = os.listdir(path)

    for item in dirs:
        if os.path.isfile(path+item):
            print(path+item)
            x = np.loadtxt(path+item, delimiter=',', unpack=True, dtype='float32')
            f, e = os.path.splitext(path+item)

            z_data = np.transpose(x[2])
            # specgram_z = stft.spectrogram(z_data)
            specgram_z = stft.spectrogram(z_data, window=0.4)
            plt._imsave(f + '.jpg', abs(specgram_z), vmin=-40, vmax=40, cmap=plt.get_cmap('coolwarm'), format='jpg') # gray Wistia






# 디렉토리 내의 파일들을 한번에 일괄 변환
convert_all_file_to_directory("/Users/User/OneDrive/센서로그/자전거/포트홀/csv/다듬다듬/")

# 스펙트럼 이미지로 일괄 변환
convert_all_file_to_spectrum("/Users/User/OneDrive/센서로그/자전거/포트홀/csv/다듬다듬/")

# 파일 하나만 스펙트럼 이미지로 바꿔줌
convert_one_file_to_spectrum("/Users/User/PycharmProjects/network/ML_Camp/Porthole_Detection/all.csv")

# 파일 하나만 바꿔줌
convert_one_file_to_image("/Users/User/PycharmProjects/network/ML_Camp/Porthole_Detection/all.csv")















