from array import array
import random
import math


for k in range(1,1001):
    print('项', end='')
    for i in range(2):
       t = 0x4e00+int(20902*random.random())
       print(chr(t),end='')
    print('', end=',')
    if (k % 10==0):
        print(' --',k)

