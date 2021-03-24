#!/usr/bin/python
# -*- coding: cp936 -*-


import io
import os

with open('test.txt', 'w') as file:
    file.write('Spam and eggs!')
    file.close()
print('a file was saved !')

has= os.path.exists("test.txt")
if has:
    f = open("test.txt", "w", encoding="cp936")
    f.write('Tea and eggs !')
    f.close()

    f = open("test.txt", "r", encoding="cp936")
    print('In the file ,text is :\n',f.read())
    f.close()


