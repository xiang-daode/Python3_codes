#!/usr/bin/python
# -*- coding: cp936 -*-

#对字节型数组赋值:
a=bytearray.fromhex("20f0 F1f2 2040 a7b8") 
print(a)

#将字节型数组转化为16进制串:
b=bytearray(b"\xf0\xf1\xf2 @\xa7\xb8").hex()
print(b) 

#将字节型数组转化为16进制串:
b=bytearray(b"\x4e\x00").hex()
print(b)


