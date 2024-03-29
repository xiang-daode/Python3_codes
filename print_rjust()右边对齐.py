# 字符串的右边对齐:
for x in range(1, 11):
     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     print(repr(x*x*x).rjust(4))

# 数值的右边对齐:
for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
