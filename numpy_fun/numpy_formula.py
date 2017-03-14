import numpy as np

# initialization variable
x = np.mat(
    [ [1,2,3],
      [3,4,5]
    ]
)

y = np.ones((2,3))

# 曼哈顿距离
print(np.sum(np.abs(x-y)))

# 欧式距离
print(np.sqrt(np.sum((x-y)*(x-y).T)))

# 闵可夫斯基距离

# 切比雪夫距离
print(np.abs(x-y).max())

# 余弦距离
print(np.sum(np.dot(x,y.T))/(np.linalg.norm(x)*np.linalg.norm(y)))

# 汉明距离(hamming distance)
matV = np.mat([ [1,1,1,1],[1,0,0,1] ])
smstr = len(np.nonzero(matV[0]-matV[1])[1])
print(smstr)
