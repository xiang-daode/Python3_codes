# 在这里写上你的代码 :-)
#
a=float(input("输入一个整数,判断是不是5的倍数:"))
v='---yes----' if a%5==0 else 'no'
print(a,v)


for a in range(1,101):
	v='---yes' if a%5==0 else 'no'
	print(a,v)
