# -*- coding: utf-8 -*-
# titanic predication

import pandas as pd
import numpy as np

# keras
from keras.models import Sequential
from keras.layers import Dense,Activation
# sk learn


if __name__ == "__main__":
    # load data
    train_data = pd.read_csv('train.csv')
    test_data = pd.read_csv('test.csv')

    # drop unnecessary columns
    train_data = train_data.drop(['PassengerId','Name','Ticket'],axis=1)
    test_data = test_data.drop(['PassengerId','Name','Ticket'],axis=1)
    # print(train_data.head())

    # declare X and Y train data
    X_train = train_data.drop('Survived',axis=1)
    Y_train = train_data['Survived']

    # declare X test data
    X_test = test_data
    print(X_train.head(),'\n',Y_train.head(),'\n',X_test.head())

    # init model
    model = Sequential()
    # layer 1
    model.add(Dense(12,input_dim=8))
    model.add(Activation('sigmoid'))
    # layer 2
    model.add(Dense(1))
    model.add(Activation('softmax'))

    # compile model
    #TODO fit model
    #TODO elvalue model
    #TODO show result
    #TODO sklearn part

