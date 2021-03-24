# 在这里写上你的代码 :-)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math

# 将完全平方数放入列表list中:
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
newlist = filter(is_sqr, range(1, 101))
print(list(newlist ))

# 将奇数放入元组tuple中:
def is_odd(n):
    return n % 2 == 1
newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(tuple(newlist))

# 将10的倍数放入集合set中:
def is_end0(n):
    return n % 10 == 0
newlist = filter(is_end0, [1, 20, 3, 40, 5, 60, 7, 80, 9, 10])
print(set(newlist))
