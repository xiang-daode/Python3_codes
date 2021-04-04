# 1~9999以'88'开头的统计
import string

c=0
for i in range(1, 9999+1):
    ln = len(str(i))
    if ln>=2 and str(i).startswith('88'):
        print(i)
        c+=1
print("Count=",c)
