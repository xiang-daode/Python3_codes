#!/usr/bin/python
# -*- coding: cp936 -*-

b= [x for x in range(2,100) if not[y for y in range(2,int(x**0.5)) if not x%y]]
print("100���ڵ�ȫ�������ǣ�",b)

c= [y for y in range(2,36)]
print('2--35ȫ�����',c)

b= [x for x in range(2,24) if True]
print('2--23ȫ�����',b)

d= [x for x in range(2,24) if False]
print('�޷��أ� ',d)

d= [x for x in range(1,25) if x%2]
print('�����У�',d)

d= [x for x in range(1,25) if not x%5]
print('5�ı����У�',d)
