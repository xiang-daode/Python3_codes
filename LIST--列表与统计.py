# LIST--列表与统计

A=[11,25,36,8,6,77,222,88,54,65,98,35,14,87,26,532,1,-9,-8,-22]
a=len(A);print("元素的数目:",a)
b=max(A);print("最大的元素:",b)
c=min(A);print("最小的元素:",c)
d=sum(A);print("求和:",d)
e=sum(A)/len(A);print("平均数:",e)
B=sorted(A);print("排序(从小到大)",B)
print("前5个元素:",B[0:5])
print("后5个元素:",B[-1:-6:-1])
C=sorted(A,reverse=True);print("排序(倒序,逆序:从大到小)",C)

#A中每一元素都乘以1.2:




