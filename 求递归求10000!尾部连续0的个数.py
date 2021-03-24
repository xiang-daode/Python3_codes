
import sys

#修改最大递归层数到30000
sys.setrecursionlimit(30000)
print(sys.getrecursionlimit()) #打印最大递归层数：30000

'''
计算10000!的结果中,末尾连续有多少个'0'
算法:将每次除以5的整商求和
答案:2499
'''
n=10000
s=0
def getQ(n):
        global s
        q=n//5
        s=s+q
        if q>0:
                getQ(q)
getQ(n)
print(s)
        
	  	
       
