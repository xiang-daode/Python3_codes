import os
import shutil
import glob
import sys


cwd=os.getcwd()      # Return the current working directory
print('====================\r\n当前目录是：',cwd)

print(glob.glob('*.py')) #列出所有*.py文件
print(glob.glob('*.txt')) #列出所有*.txt文件

print('====================\r\n当前目录与文件名是：')
print(sys.argv)
