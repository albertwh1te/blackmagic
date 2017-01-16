# -*- coding: utf-8 -*-
# titanic predication with neural network

import numpy as np
import pandas as pd

if __name__ == "__main__":
    # keras
    from keras.models import Sequential
    from keras.layers import Dense,Activation

    from pre_process import X_train,Y_train,X_test,train_raw,test_raw

    # init model
    model = Sequential()

    # # layer 1
    model.add(Dense(12,input_shape=(7,)))
    model.add(Activation('relu'))
    # # # # layer 2
    model.add(Dense(8))
    model.add(Activation('relu'))
    # # # layer3
    model.add(Dense(1))
    model.add(Activation('sigmoid'))


    # compile model
    # model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=["accuracy"])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


    # fit model
    model.fit(X_train, Y_train, nb_epoch=150, batch_size=10, verbose=2)

    # elvalue model
    loss,accuracy = model.evaluate(X_train,Y_train,verbose=2)

    # show accuracy
    print(accuracy)

    # network_pred = model.predict(X_test,batch_size=10,verbose=2)
    network_pred = model.predict_classes(X_test,batch_size=10,verbose=2)
    # print(network_pred)

    # print(submission.head())
    submission = np.hstack([test_raw['PassengerId'].as_matrix().reshape(418,1),network_pred])
    submission = pd.DataFrame(submission)
    submission.to_csv('result_network_titanic.csv',index=False)
