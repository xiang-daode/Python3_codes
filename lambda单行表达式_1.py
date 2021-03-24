import numpy as np


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print ([x * 2 + 10 for x in foo]) #表达式运算
print ([x % 2 for x in foo]) #奇偶性
print ([x // 10 for x in foo]) #看十位上的数
print ([x <<2 for x in foo]) #乘以4
print ([np.cos(x)  for x in foo]) #表达式运算
