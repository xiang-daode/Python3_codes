#!/usr/bin/python
# -*- coding: cp936 -*-

from math import sqrt

#1000以内的质数--1,全部打印: 
#print(" ".join("%s"% x for x in range(2,1000)if not[y for y in range(2,int(sqrt(x)))if not x%y]))

#质因数分解--2：
b=int(input('输入任意正整数='))
mylist=[]
def func(a):
    for i in range(2,a):
        if a%i==0:
            mylist.append(i)
            a=a//i
            return func(a)
    mylist.append(a)
    if len(mylist)>1:
        print('{}能分解为{}'.format(b,mylist))
    else:
        print('{}是质数'.format(a))
 
func(b)

