#!/usr/bin/python
# -*- coding: cp936 -*-

#���ֽ������鸳ֵ:
a=bytearray.fromhex("20f0 F1f2 2040 a7b8") 
print(a)

#���ֽ�������ת��Ϊ16���ƴ�:
b=bytearray(b"\xf0\xf1\xf2 @\xa7\xb8").hex()
print(b) 

#���ֽ�������ת��Ϊ16���ƴ�:
b=bytearray(b"\x4e\x00").hex()
print(b)


