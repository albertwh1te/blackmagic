# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd


# let us to do it in a proper way

def data_clean(df):
    df['Gender'] = df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)

    df["Fare"].fillna(df["Fare"].median(), inplace=True)

    df['AgeIsNull'] = pd.isnull(df.Age).astype(int)

    average_age_titanic   = df["Age"].mean()
    std_age_titanic       = df["Age"].std()
    count_nan_age_titanic = df["Age"].isnull().sum()

    # generate random numbers between (mean - std) & (mean + std)
    rand_1 = np.random.randint(average_age_titanic - std_age_titanic,
                               average_age_titanic + std_age_titanic,
                               size = count_nan_age_titanic)


    # fill NaN values in Age column with random values generated
    df["Age"][np.isnan(df["Age"])] = rand_1

    # convert from float to int df['Age'] = df['Age'].astype(int)

    df = df.drop(['Name','Sex','Ticket','Embarked','Cabin'],axis=1)
    return df

def feature_engineering(df):
    df['FamilySize'] = df['SibSp'] + df['Parch']
    df['Age*Class'] = df.Age * df.Pclass
    return df


train_data = pd.read_csv("data/train.csv",header=0)
test_data = pd.read_csv("data/test.csv",header=0)

# print(train_data.head())
cleaned_test = data_clean(test_data)
cleaned_train = data_clean(train_data)

featured_test = feature_engineering(cleaned_test)
featured_train = feature_engineering(cleaned_train)

# print(featured_train.head(),featured_test.head())
# print(featured_train.head())
# print(featured_test.head())

X_train = featured_train.drop(["PassengerId","Survived"],axis=1)
Y_train = featured_train["Survived"]
print(X_train.head())
print(Y_train.head())

X_test = featured_test.drop(["PassengerId"],axis=1)
# X_test = featured_test.values
print(X_test.head())

# Sklearn Part
from sklearn.model_selection import cross_val_score


# svm
from sklearn import svm

# set cv
from sklearn.model_selection import GridSearchCV,StratifiedShuffleSplit
cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)

# # train without set
# rbf_svm = svm.SVC()
# rbf_svm.fit(X_train,Y_train)
# score = cross_val_score(rbf_svm,X_train,Y_train,cv=cv).mean()
# print(score)

# # set grid space
# C_range = np.logspace(-2, 5, 13)
# gamma_range = np.logspace(-9, 3, 13)
# param_grid = dict(gamma=gamma_range, C=C_range)

# # find parameter
# grid = GridSearchCV(svm.SVC(), param_grid=param_grid, cv=cv,n_jobs=3,verbose=2)
# print('start')
# grid.fit(X_train,Y_train)
# print("The best parameters are %s with a score of %0.2f"
#   % (grid.best_params_, grid.best_score_))

# rbf_svm_new = svm.SVC(**grid.best_params_)
# rbf_svm_new.fit(X_train,Y_train)
# score = cross_val_score(rbf_svm_new,X_train,Y_train,cv=cv).mean()
# print(score)



# score = rbf_svm.score(X_train,Y_train)

# new_pred = rbf_svm_new.predict(X_test)
# submission = pd.DataFrame({
#     "PassengerId":featured_test["PassengerId"],
#     "Survived":new_pred
# })
# submission.to_csv('result_svm_new_titanic.csv',index=False)

# random forest

from sklearn.ensemble import RandomForestClassifier

#     rf_params = {
#     'n_jobs': -1,
#     'n_estimators': 500,
#      'warm_start': True,
#      #'max_features': 0.2,
#     'max_depth': 6,
#     'min_samples_leaf': 2,
#     'max_features' : 'sqrt',
#     'verbose': 3
# }
#origin model
RF_clf = RandomForestClassifier(
    # n_estimators=500,
    # **rf_params
)

RF_clf.fit(X_train,Y_train)
# print(X_train)
# RF_clf.fit(X_train[0::,1::],X_train[0::,0])

score = RF_clf.score(X_train,Y_train)
score = cross_val_score(RF_clf,X_train,Y_train,cv=5).mean()
print(score)


#paramers search
n_estimators = [1000]
criterion = ['gini','entropy']
max_features = np.logspace(-2,0,50)
param_grid = dict(
    n_estimators=n_estimators,
    max_features=max_features,
    criterion=criterion
)
grid = GridSearchCV(
    RandomForestClassifier(),
    param_grid=param_grid,
    cv=cv,
    n_jobs=3,
    verbose=2
)
grid.fit(X_train,Y_train)
print("The best parameters are %s with a score of %0.2f"
    % (grid.best_params_, grid.best_score_))

RF_clf = RandomForestClassifier(
    n_jobs=3,
    **grid.best_params_
)
RF_clf.fit(X_train,Y_train)
random_forest_pred = RF_clf.predict(X_test)
score = cross_val_score(RF_clf,X_train,Y_train,cv=cv).mean()
print(score)
# print(random_forest_pred)

submission = pd.DataFrame({
    'PassengerId':featured_test['PassengerId'],
    'Survived':random_forest_pred
})
submission.to_csv('random_forest_new_titanic.csv',index=False)


# # LogisticRegression
#     from sklearn.linear_model import LogisticRegression
#     LR_clf = LogisticRegression()
#     LR_clf.fit(X_train,Y_train)
#     score = cross_val_score(LR_clf,X_train,Y_train,cv=5).mean()
#     print(score)



