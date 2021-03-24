
import sys

#修改最大递归层数到30000
sys.setrecursionlimit(30000)
print(sys.getrecursionlimit()) #打印最大递归层数：30000

'''
10进制转2进制
'''
n=255
s=[]
def getQ(n):
        global s
        q=n//2
        r=n % 2
        s.insert(0,hex(r))  #从前面插入, 若从尾部插入用: s.append(hex(r))
        if q>0:
                getQ(q)
getQ(n)
print(s)
        
	  	
       
