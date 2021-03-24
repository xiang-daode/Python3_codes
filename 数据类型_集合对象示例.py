# 在这里写上你的代码 :-)


# 列表 list	========================
x = ["apple", "banana", "cherry"]	
print(x)
x = [33,44,55,66,77]	# 列表 list	
print(x[0],x[4])

# 元组 tuple	=============================
x = ("apple", "banana", "cherry")	
print(x)
x = "bee", "cat", "dog","fox"	# 元组 tuple	
print(x[-1],x[-2])
a,b,c=1,2,3
print(a+b,b+c,c+a)

# 区间,范围  range	=============================
x = range(6)	
print(x)
x = range(2,8)	# 区间,范围  range	
print(x)
x = range(2,12,2)	# 区间,范围  range	
print(x[4])

# 集合 set	==============================
x = {"apple", "banana", "cherry"}	
print(x)
x = {11,22,33,44,55}	
print(x)
y=sorted(x)
print(y)
z=list(reversed(y))
print(z)
# 当集合不可变时，它就满足了作为集合中的元素的要求，就可以放在另一个集合中了
x1 = frozenset({"apple", "banana", "cherry"})	#返回一个新的冻结的集合 frozenset	
print(x1)
x2 = frozenset({5,4,3,2,1})	#返回一个新的冻结的集合 frozenset	
print(x2)
y={x1,x2,"集合,看我的!"}
print(y)


# 字典 dict	=============================
x = {"name" : "daode",  "age": 62}	
x["high"]= 173
x["weight"]=72
print(x)
print(x["name"],x["high"],x["age"])
