#!/usr/bin/python
# -*- coding: cp936 -*-


import io
import os

with open('test.txt', 'w') as file:
    file.write('Spam and eggs!')

print('a file was saved !')

has= os.path.exists("test.txt")
if has:
    f = open("test.txt", "r", encoding="cp936")
    print('In the file ,text is :\n',f.read())
