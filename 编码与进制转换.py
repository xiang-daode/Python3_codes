#!/usr/bin/python
# -*- coding: cp936 -*-


print(0b1010) #2����==>10����
print(int('1010',2)) #2����==>10����
print(int('FFFF',16)) #16����==>10����
print('65536-->',bin(65536))#10����==>2����
print('16777216-->',bin(16777216))

print('65536-->',hex(65536))#10����==>16����
print('16777216-->',hex(16777216))

print(0xFFFF) #16����==>10����
print(0xffffff)

print(ascii('��')) #  \u9879  
print(ascii('��')) #  \u9053
print(ascii('��')) #  \u5fb7

s='\u9879\u9053\u5fb7'
print(s)  #�����

print(chr(0x9879),chr(0x9053),chr(0x5fb7))  #�� �� ��


s="\\u0063\\u0072\\u0069\\u0066\\u0061\\u006E\\u0020\\u5728\\u8DEF\\u4E0A"
# crifan ��·��

s='\\u9879\\u9053\\u5fb7' #�����

#�������ֱ������:
s2=s.encode('utf-8').decode('unicode_escape')
print(s2)


