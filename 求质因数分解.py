#!/usr/bin/python
# -*- coding: cp936 -*-

from math import sqrt

#1000���ڵ�����--1,ȫ����ӡ: 
#print(" ".join("%s"% x for x in range(2,1000)if not[y for y in range(2,int(sqrt(x)))if not x%y]))

#�������ֽ�--2��
b=int(input('��������������='))
mylist=[]
def func(a):
    for i in range(2,a):
        if a%i==0:
            mylist.append(i)
            a=a//i
            return func(a)
    mylist.append(a)
    if len(mylist)>1:
        print('{}�ֽܷ�Ϊ{}'.format(b,mylist))
    else:
        print('{}������'.format(a))
 
func(b)

