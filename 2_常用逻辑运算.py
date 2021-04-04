# 单行判断与变量的赋值:
a = [1,2,3]
b = a if len(a) != 0 else ""
print(b)

c=[]
d = c if len(c) != 0 else "c 是一个空列表"
print(d)

a = [1,2,3]
b = 4 if 4 not in a else 100
print(b)

a = [1,2,3]
b = 3 if 3 in a else 100
print(b)
