# -*- coding: utf-8 -*-
# titanic predication with support vector machine


import numpy as np
import pandas as pd


if __name__ == "__main__":
    from pre_process import X_train,Y_train,X_test,train_raw,test_raw
    from sklearn import SVC
