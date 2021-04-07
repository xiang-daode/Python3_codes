
import numpy as np


# 系数矩阵:
a = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
b = np.array([1,2, 3, 4])

# 在表达式 A*X=B 中求出X:
X = np.linalg.solve(a, b)

# 输出:
print(X) #[1. 2. 3. 4.]



