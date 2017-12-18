import numpy as np
import pandas as pd
import os


def load_all_files(path):

    dirs = os.listdir(path)

    for item in dirs:
        if os.path.isfile(path+item):
            print(path+item)
            x = np.loadtxt(path+item, delimiter=',', unpack=True, dtype='float32')
            f, e = os.path.splitext(path+item)


load_all_files('C:/Users/User/Desktop/Pothole_Detection_using_CNN/Sensor_data/자동차/아스팔트/')