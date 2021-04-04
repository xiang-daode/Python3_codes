# 在这里写上你的代码 :-)
import numpy as np

# 列表对象转数组:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 下标是偶数时乘以5,下标是奇数时修改值为-1:
arr[arr % 2 == 1]*=5
arr[arr % 2 == 0]=-1

print(arr)


