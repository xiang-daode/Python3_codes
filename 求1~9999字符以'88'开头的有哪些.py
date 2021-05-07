# 1~9999以'88'开头的统计
import string

#解法一:运用字符串函数:
c=0
for i in range(1, 9999+1):
    ln = len(str(i))
    if ln>=2 and str(i).startswith('88'):
        #print(i)
        c+=1
print("Count=",c)



#解法二:运用数学特征:
c=0
for i in range(1, 9999+1):    
    if i>1000 and i//100==88:
        #print(i)
        c+=1
    elif i>100 and i//10==88:
        c+=1
    # i<100: 88
    
print("Count=",c+1)
