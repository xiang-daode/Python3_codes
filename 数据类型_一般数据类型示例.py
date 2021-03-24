# 在这里写上你的代码 :-)
# 一般数据类型:================================
x = "Hello World"	# 字符串 str	
print(x)
print(x[0])
print(x[-1])
print(x[0:4]) # 范围是0,1,2,3.  4不可到达
print(x[0:11:2]) # 范围是[0,...,11),11不可到达
y=reversed(x)
print(list(y))
x="一"
print(ascii(x),ord(x),hex(ord(x)),x.encode("GBK"),x.encode("UTF-8"))

# 整数 int	=========================================
x = 16777215,65535,255	# 整数 int	
print(x)
print(hex(x[0]),hex(x[1]),hex(x[2]))
print(bin(15))
print(bin(32767))
print(min(x),max(x),sum(x))
print(sorted(x))


# 浮点数 float	===============================
x,y,z =2.71828,1.4142, 3.1416	# 3个浮点数 float	
print(z,y,x)
x=8**(1/3)   # 分数,小数作为指数
print(x)
x=0.01**(-2) # 负数作为指数
print(x)
x=pow(8,1/3)   # 分数,小数作为指数
print(x)
x=pow(0.01,-2) # 负数作为指数
print(x)
x=abs(-9)
print(x)
print(3*3+4*4+100*0.75)


# 复数 complex	================================
x = 3+4j	# 复数 complex	
y = 3-4j	# 复数 complex	
print(x,y,1/x,1/y,x*y,x/y)

# 逻辑型 bool ====================================	
x = True	# 逻辑型 bool	
print(x)
x = False	# 逻辑型 bool	
print(x)
x = (3>2)	# 逻辑型 bool	
print(x)
x = (99>100)	# 逻辑型 bool	
print(x)
x = (4*25==100)	# 逻辑型 bool	
print(x)
print(not True,True or False,True and True) #逻辑运算
print(25 ^ 75,25 | 75,25 & 75, ~1) #按位运算
