#!/usr/bin/python
# -*- coding: cp936 -*-


import io
import os

'''
#���´����ļ�,��д������:
with open('test.txt', 'w') as file:
    file.write('Spam and eggs!')

print('a file was saved !')
'''


has= os.path.exists("test.txt")
if has:
    f = io.FileIO("test.txt", "a")
    f.write(b'anji Tea and eggs !') #�����Զ����Ʒ�ʽ׷������
    f.close()
    
    #��ȡ�ļ�����:
    f = open("test.txt", "r", encoding="cp936")
    print('In the file ,text is :\n',f.read())
    f.close()


