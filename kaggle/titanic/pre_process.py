# -*- coding: utf-8 -*-


# preposses data for titanic

# titanic predication
from random import randint
import pandas as pd
import numpy as np
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

# set None age
train_data["Age"].fillna(train_data["Age"].median(), inplace=True)
test_data["Age"].fillna(test_data["Age"].median(), inplace=True)

# set None data in test data("Fare")
test_data["Fare"].fillna(test_data["Fare"].median(), inplace=True)

# declare X and Y train data
X_train = train_data.drop(['Survived'],axis=1).as_matrix()
Y_train = train_data['Survived'].as_matrix()

# declare X test data
X_test = test_data.as_matrix()

if __name__ == "__main__":
    print(train_data.head())
    print(test_data.head())
