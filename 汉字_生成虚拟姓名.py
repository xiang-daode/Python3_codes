from array import array
import random
import math

for k in range(400):
    t1 = int(20902*random.random())
    t2 = int(20902*random.random())
    p1 = 0x4e00 + t1
    p2 = 0x4e00 + t2
    print('项',chr(p1),chr(p2))

'''
a = array('H', [0x4e00, 0x5577, 0x9fa5])
print(chr(a[0]), chr(a[1]), chr(a[2]))
print(hex(ord('一')))
print(hex(20902+0x4e00))
print(hex(ord('项')))
print(hex(ord('道')))
print(hex(ord('德')))
'''