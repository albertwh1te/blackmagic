# -*- coding: utf-8 -*-
# titanic predication with random forest


import numpy as np
import pandas as pd

if __name__ == "__main__":
    from pre_process import X_train,Y_train,X_test,Y_test,test_raw,X_pred
    from sklearn.ensemble import RandomForestClassifier

    RF_clf = RandomForestClassifier()

    RF_clf.fit(X_train,Y_train)

    score = RF_clf.score(X_test,Y_test)
    print(score)

    random_forest_pred = RF_clf.predict(X_pred)

    submission = pd.DataFrame({
        'PassengerId':test_raw['PassengerId'],
        'Survived':random_forest_pred
    })
    submission.to_csv('random_forest_titanic.csv',index=False)
