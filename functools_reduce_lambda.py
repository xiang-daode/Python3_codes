# 在这里写上你的代码 :-)
from functools import reduce

lst = [1, 2, 3, 4, 5]
f_res = filter(lambda x: x>3, lst)
d_res = reduce(lambda x, y: x+y, lst)
r_res = reduce(lambda x, y: x*y, lst)
x_res = reduce(lambda x, y: x^y, lst)

print('大于3的数字有：', list(f_res))
print('累加结果为：', d_res)
print('累乘结果为：', r_res)
print('累异或结果为：', x_res)

