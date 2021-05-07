# 1~9999以'44'结尾的统计
import string

#方法1,使用字符串函数如下:
c=0
for i in range(1, 9999+1):
    ln = len(str(i))
    if ln>=2 and str(i).endswith('44'):
        #print(i)
        c+=1
print("Count=",c)

#方法1,使用数学特征如下:
c=0
for i in range(1, 9999+1):    
    if i % 100==44:
        #print(i)
        c+=1
print("Count=",c)
