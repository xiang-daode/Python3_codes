from array import array
import random
import math

for k in range(100):
    for i in range(7):
       t = 0x4e00+int(20902*random.random())
       print(chr(t),end='')
    print()

'''
a = array('H', [0x4e00, 0x5577, 0x9fa5])
print(chr(a[0]), chr(a[1]), chr(a[2]))
print(hex(ord('一')))
print(hex(20902+0x4e00))
'''