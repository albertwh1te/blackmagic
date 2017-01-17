# -*- coding: utf-8 -*-
# titanic predication with support vector machine


import numpy as np
import pandas as pd


if __name__ == "__main__":
    from pre_process import X_train,Y_train,X_test,Y_test,test_raw,X_pred
    from sklearn import svm
    # kernel rbf means Gaussian
    rbf_svm = svm.SVC(kernel='rbf')

    print(X_train[:5],Y_train[:5])
    rbf_svm.fit(X_train,Y_train)
    score = rbf_svm.score(X_test,Y_test)
    print(score)

    rbf_svm_pred = rbf_svm.predict(X_pred)

    submission = pd.DataFrame({
        'PassengerId':test_raw['PassengerId'],
        'Survived':rbf_svm_pred
    })
    submission.to_csv('rbf_svm_titanic.csv',index=False)
