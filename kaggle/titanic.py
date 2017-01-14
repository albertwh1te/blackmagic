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

    # Preprocess Part

    # drop unnecessary columns
    train_data = train_data.drop(['PassengerId','Name','Ticket','Embarked','Cabin'],axis=1)
    # preprocess test data
    test_data = test_data.drop(['PassengerId','Name','Ticket','Embarked','Cabin'],axis=1)

    # get dummies on sex
    sex_dummies = pd.get_dummies(train_data['Sex'])
    sex_dummies.columns = ['Male','Female']
    print(sex_dummies)
    # train_data.join(sex_dummies)
    train_data = pd.concat([train_data,])

    # train_data = train_data.drop(['Sex'],axis=1)

    print(train_data.head())


    # declare X and Y train data
    X_train = train_data.drop('Survived',axis=1).as_matrix()
    Y_train = train_data['Survived'].as_matrix()

    # print(X_train)
    # declare X test data
    X_test = test_data
    # print(X_train.head(),'\n',Y_train.head(),'\n',X_test.head())
    print(len(X_train))

    # init model
    model = Sequential()

    # # layer 1
    # model.add(Dense(12,input_dim=8))
    # model.add(Activation('sigmoid'))
    # # layer 2
    # model.add(Dense(3))
    # model.add(Activation('softmax'))

    model.add(Dense(12, input_dim=7, init='uniform', activation='relu'))
    model.add(Dense(8, init='uniform', activation='relu'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))



    # compile model
    # model.complie(optimizer='adam',loss='c')

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=["accuracy"])

    #TODO fit model
    model.fit(X_train, Y_train, nb_epoch=100, batch_size=10, verbose=0)

    #TODO elvalue model
    loss,accuracy = model.evalute(X_train,Y_train,verbose=0)
    #TODO show result
    print(loss,'\n',accuracy)
    #TODO sklearn part

