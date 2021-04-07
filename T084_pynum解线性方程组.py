# 在这里写上你的代码 :-)

import numpy as np

#我们首先构建A和b的数组,方程是 Ax=b:
A = np.array([
[1,0,0],
[1,1,0],
[1,1,1]
])
b = np.transpose(np.array([[1,3,6]]))

#求线性方程组的解:
x = np.linalg.solve(A,b)
#打印解向量(列表)
print(x)
'''线性方程组的解:
[[1.]
 [2.]
 [3.]]
'''

print(help(np.linalg.solve))
