;import numpy as np
np.random.seed(1337)

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten,Convolution2D,MaxPooling2D
from keras.utils import np_utils


#取得数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#展示数据
digit_nums = X_train[:40]

import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
for digit_num in range(40):
    plt.subplot(4,10,digit_num+1)
    grid_data = digit_nums[digit_num]
    plt.imshow(grid_data, interpolation = "none", cmap = "afmhot")
    plt.xticks([])
    plt.yticks([])
# plt.show()

#处理数据

#one hot encoding
Y_train = np_utils.to_categorical(y_train,nb_classes=10)
Y_test = np_utils.to_categorical(y_test,nb_classes=10)

#TODO make function
#把mnist 的数据变为图片张量，格式为([samples][width][height][pixels]),顺便改为内存占用更少的32 bits
X_train = X_train.reshape(X_train.shape[0], 28, 28,1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28,1).astype('float32')
# def preproc(data,target)

# feature scaling
# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255

# input image dimensions
img_rows, img_cols = 28, 28
# number of convolutional filters to use
nb_filters = 32
# size of pooling area for max pooling
pool_size = (2, 2)
# convolution kernel size
kernel_size = (3, 3)
nb_classes = 10
batch_size = 128
nb_classes = 10
nb_epoch = 20
input_shape = (img_rows, img_cols, 1)

# 建立model 函数
def model_factory(layers):
    model = Sequential()
    # map(lambda x:model.add(x),layers)
    for i in layers:
        print(i)
        model.add(i)
    return model

#神经网络架构(Convolutional Layer, Pooling Layer, and Fully-Connected Layer)
layers = [
    #第一卷积层
    Convolution2D(nb_filters, kernel_size[0], kernel_size[1],
                        border_mode='valid',
                        input_shape=input_shape),
    Activation('relu'),
    #第二卷积层
    Convolution2D(32,3,3),
    Activation('relu'),
    #max pooling 层
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),
    #FC 层
    Flatten(),
    Dense(128),
    Activation('relu'),
    Dropout(0.5),
    #输出层
    Dense(10),
    Activation('softmax')
]

model = Sequential()
model.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1],
                        border_mode='valid',
                        input_shape=input_shape))
model.add(Activation('relu'))
model.add(Convolution2D(nb_filters, kernel_size[0], kernel_size[1]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=pool_size))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

#训练
# model = model_factory(layers)
print(model)
model.compile(loss='categorical_crossentropy',
              optimizer='adadelta',
              metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=nb_epoch,
          verbose=1, validation_data=(X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
;
