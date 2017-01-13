# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

# keras
from keras.models import Sequential
from keras.layers import Dense


if __name__ == "__main__":
    # load data
    tran_data = pd.read_csv('train.csv')
    test_data = pd.read_csv('test.csv')
    print(tran_data.head())

