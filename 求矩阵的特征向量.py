# 用消元法求矩阵的特征向量

import numpy as np
A = np.array([[1,2,3,],[4,4,4],[3,2,1]])
a,b= np.linalg.eig(A)
print(format(b))
