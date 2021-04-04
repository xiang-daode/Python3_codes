import os
import shutil

cwd=os.getcwd()      # Return the current working directory
print(cwd) #当前文件的路径

m=cwd.index('\\')
print(cwd[0:m]) #当前文件的路径,取出盘符

n=cwd.rindex('\\')+1
print(cwd[n:]) #最后的文件夹名

print(__file__) #全部路径,包含文件全名

s=__file__.rindex('\\')+1
print(__file__[s:]) #文件名



