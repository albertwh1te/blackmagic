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

    # convert from float to int
    df['Age'] = df['Age'].astype(int)

    df = df.drop(['Name','Sex','Ticket','Embarked','Cabin'],axis=1)
    return df

def feature_engineering(df):
    df['FamilySize'] = df['SibSp'] + df['Parch']
    df['Age*Class'] = df.Age * df.Pclass
    return df


if __name__ == '__main__':
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

    # X_train = featured_train.drop(["PassengerId","Survived"],axis=1)
    X_train = featured_train.values
    # Y_train = featured_train["Survived"]
    # Y_train = featured_train["Survived"]
    # print(X_train.head())
    # print(Y_train.head())

    # X_test = featured_test.drop(["PassengerId"],axis=1)
    X_test = featured_test.values
    # print(X_test.head())

#svm
    # from sklearn import svm
    # # kernel rbf means Gaussian
    # rbf_svm = svm.SVC(kernel='rbf')

    # rbf_svm.fit(X_train,Y_train)
    # score = rbf_svm.score(X_train,Y_train)
    # print(score)

    # new_pred = rbf_svm.predict(X_test)
    # submission = pd.DataFrame({
    #     "PassengerId":featured_test["PassengerId"],
    #     "Survived":new_pred
    # })
    # submission.to_csv('result_svm_new_titanic.csv',index=False)

# random forest

    from sklearn.ensemble import RandomForestClassifier

    RF_clf = RandomForestClassifier(
        n_estimators=500,
    )

    # RF_clf.fit(X_train,Y_train)
    print(X_train)
    RF_clf.fit(X_train[0::,1::],X_train[0::,0])

    # score = RF_clf.score(X_train,Y_train)
    # print(score)

    random_forest_pred = RF_clf.predict(X_test)
    # print(random_forest_pred)

    submission = pd.DataFrame({
        'PassengerId':featured_test['PassengerId'],
        'Survived':random_forest_pred
    })
    submission.to_csv('random_forest_new_titanic.csv',index=False)

