# 在这里写上你的代码 :-)
# 一般数据类型:================================
x = "Hello World"	# 字符串 str	
print(x)
x = 29	# 整数 int	
print(x)
x = 3.14159265	# 浮点数 float	
print(x)
x = 3+2j	# 复数 complex	
print(x)
x = True	# 逻辑型 bool	
print(x)

# 集合对象:=======================================
x = ["apple", "banana", "cherry"]	# 列表 list	
print(x)
x = ("apple", "banana", "cherry")	# 元组 tuple	
print(x)
x = range(6)	# range	
print(x)
x = {"name" : "Bill", "age" : 63}	# 字典 dict	
print(x)
x = {"apple", "banana", "cherry"}	# 集合 set	
print(x)
x = frozenset({"apple", "banana", "cherry"})	#冻结的集合 frozenset	
print(x)

# 内码与字节:=========================================
x = b"Hello"	# 字节型 bytes	
print(x)
x = bytes(4)	# 4个不可修改字节型数组 byte	
print(x)
x = bytes("项,道,德","cp936")	# 以拼音为序, 3个不可修改字节型数组 byte	
print(1,x)
x = bytearray(4)	# 4个可修改字节型数组 bytearray	
print(x)
x ='项,道,德'.encode('gbk') # 以拼音为序, 3个可修改字节型数组 bytearray	
print(2,x)
x = bytearray("项 道 德","UTF8")	# 3个可修改字节型数组 bytearray	
print(3,x)
x = ascii("项 道 德")	# 3个可修改字节型数组 bytearray	
print(4,x)
x =  ord("项"), ord("道"),ord("德")	# 3个可修改字节型数组 bytearray	
print(5,x)

# 内存读取:=============================================
x = memoryview(bytes(3))	# 查看内存 memoryview	
print(x) #返回内存地址
x= memoryview(bytearray("abcefg", 'utf-8'))
print(x,x[2],x[-2],x[1:5],x[1:5].tobytes())# 注意下标用法	
