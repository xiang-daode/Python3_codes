# 1~9999以'44'结尾的统计
import string

c=0
for i in range(1, 9999+1):
    ln = len(str(i))
    if ln>=2 and str(i).endswith('44'):
        print(i)
        c+=1
print("Count=",c)
