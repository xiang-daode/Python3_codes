# 范围,区间: range(起点,终点,步长(+或-))
a1=range(10) #0,1,...,9
print(tuple(a1)) #用元组方式显示
print(list(a1)) #用列表方式显示
print(a1[9])#下标是从0开始的

a2=range(1,101,2) #100以内的奇数
print(list(a2))

a3=range(5,501,5) #500以内5的倍数
print(tuple(a3))
