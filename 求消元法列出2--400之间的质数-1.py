'''
采用消元法列出2--400之间的质数

'''


import random
import numpy as np

n=400

#数组初始化:
a=np.arange(0,401) 
for i in range(1,n+1):
    a[i]=i


#若其后的整数成为当前整数的倍数,则删除之(令其值为0)
for i in range(2,n+1):
  for k in range(2,int(n**0.5)+1):
     if  i>k  and i % k==0:
         a[i]=0


#列出非零的,即是质数:
b=[]
for i in range(2,n+1):
    if  a[i]!=0:
       b.append(i)

print(b) #      

         
