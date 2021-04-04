import numpy as np

#使用范围生成数组:
arr = np.arange(10)

#第二个数组的生成:
out = np.where(arr % 2 == 1, -1, arr*arr)


#打印:
print(arr,out)

#  输出: [0 1 2 3 4 5 6 7 8 9]
#  输出: [ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1]
