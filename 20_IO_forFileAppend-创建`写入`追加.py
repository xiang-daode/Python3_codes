#!/usr/bin/python
# -*- coding: cp936 -*-


import io
import os

'''
#重新创建文件,并写入内容:
with open('test.txt', 'w') as file:
    file.write('Spam and eggs!')

print('a file was saved !')
'''


has= os.path.exists("test.txt")
if has:
    f = io.FileIO("test.txt", "a")
    f.write(b'anji Tea and eggs !') #必须以二进制方式追加内容
    f.close()
    
    #读取文件内容:
    f = open("test.txt", "r", encoding="cp936")
    print('In the file ,text is :\n',f.read())
    f.close()


