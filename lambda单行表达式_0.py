#!/usr/bin/python
# -*- coding: cp936 -*-

b= [x for x in range(2,100) if not[y for y in range(2,int(x**0.5)) if not x%y]]
print("100以内的全部质数是：",b)

c= [y for y in range(2,36)]
print('2--35全部输出',c)

b= [x for x in range(2,24) if True]
print('2--23全部输出',b)

d= [x for x in range(2,24) if False]
print('无返回： ',d)

d= [x for x in range(1,25) if x%2]
print('奇数有：',d)

d= [x for x in range(1,25) if not x%5]
print('5的倍数有：',d)
