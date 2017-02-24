# -*- coding: utf-8 -*-
# titanic predication with support vector machine


import numpy as np
import pandas as pd


if __name__ == "__main__":
    from pre_process import X_train,Y_train,X_test,train_raw,test_raw
    from sklearn import svm
    # kernel rbf means Gaussian
    rbf_svm = svm.SVC(kernel='rbf')

    rbf_svm.fit(X_train,Y_train)
    score = rbf_svm.score(X_train,Y_train)
    # print(score)

    rbf_svm_pred = rbf_svm.predict(X_test)

    submission = pd.DataFrame({
        'PassengerId':test_raw['PassengerId'],
        'Survived':rbf_svm_pred
    })
    submission.to_csv('result_svm_titanic.csv',index=False)

