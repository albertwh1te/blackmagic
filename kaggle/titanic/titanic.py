# -*- coding: utf-8 -*-
# titanic predication
from random import randint
import pandas as pd
import numpy as np

# keras
from keras.models import Sequential
from keras.layers import Dense,Activation
# sk learn


if __name__ == "__main__":
    # load data
    train_raw = pd.read_csv('data/train.csv')
    test_raw = pd.read_csv('data/test.csv')

    # Data Clean Part

    # drop unnecessary columns
    train_data = train_raw.drop(['PassengerId','Name','Ticket','Embarked','Cabin'],axis=1)
    # preprocess test data
    test_data = test_raw.drop(['PassengerId','Name','Ticket','Embarked','Cabin'],axis=1)

    # get dummies on sex
    sex_dummies_train = pd.get_dummies(train_data['Sex'])
    sex_dummies_train.columns = ['Male','Female']
    train_data = train_data.join(sex_dummies_train).drop(['Sex'],axis=1)

    sex_dummies_test = pd.get_dummies(test_data['Sex'])
    sex_dummies_test.columns = ['Male','Female']
    test_data = test_data.join(sex_dummies_test).drop(['Sex'],axis=1)

    # set none age
    train_data["Age"].fillna(train_data["Age"].median(), inplace=True)
    test_data["Age"].fillna(test_data["Age"].median(), inplace=True)

    # set None data in test data
    test_data["Fare"].fillna(test_data["Fare"].median(), inplace=True)

    print(train_data.head())
    print(test_data.head())


    # declare X and Y train data
    X_train = train_data.drop(['Survived'],axis=1).as_matrix()
    Y_train = train_data['Survived'].as_matrix()

    # declare X test data
    X_test = test_data.as_matrix()

    print(len(X_train[0]))
    print(len(X_train))

    print(X_train)
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
    print(network_pred)

    # print(type(network_pred))
    # print(submission.head())
    # print(len(network_pred),len(test_raw['PassengerId'].as_matrix()))
    # print(test_raw['PassengerId'].as_matrix().reshape(418,1))
    submission = np.hstack([test_raw['PassengerId'].as_matrix().reshape(418,1),network_pred])
    submission = pd.DataFrame(submission)
    submission.to_csv('network_titanic.csv',index=False)

    #sklearn part
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import SVC, LinearSVC
    logreg = LogisticRegression()

    logreg.fit(X_train, Y_train)

    logreg_pred = logreg.predict(X_test)

    score = logreg.score(X_train, Y_train)

    submission = pd.DataFrame({
        'PassengerId':test_raw['PassengerId'],
        'Survived':logreg_pred
    })
    submission.to_csv('logreg_titanic.csv',index=False)
    # print(score)
    # print(logreg_pred)

