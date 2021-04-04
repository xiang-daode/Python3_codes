# 在这里写上你的代码 :-)
'''
约定:X的转置用'XT'表示,A的逆用'A^-1'表示,矩阵相乘用'*'表示:

使用np.linalg.solve计算β，因为等式是：
β = (XT*X)^-1*XT*y

在数学上等价于方程组：
(XT*X)*β = XT*y

注:不存在逆阵时,常常以SVD(奇异值分解)方式处理.
'''
import numpy as np

X = np.array([
[1,-0.00909,0.001],
[1.003,1.01,-0.0097],
[1,1.001,1.007]
])
y = np.transpose(np.array([[1,3,6]]))

Xt = np.transpose(X)
XtX = np.dot(Xt,X)
Xty = np.dot(Xt,y)
beta = np.linalg.solve(XtX,Xty)

print(beta)

''' beta=
[[1.01512453]
 [1.99074466]
 [2.97134069]]
也即:
f(x,y,z)=1.01512453*x+1.99074466*y+2.97134069*z
属于"多元线性回归"
'''
