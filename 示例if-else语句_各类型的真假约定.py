# 在这里写上你的代码 :-)
#布尔类型,也叫逻辑类型: 大多视表达式,成立为真,不成立为假:
#常配合: &(and) ,|(or) ,~(not),
b = False
if b:
    print('b是True')
else:
    print('b是False')

b2 = (3<5)&(3+6==9)and(1+1==2)
if b2:
    print('b2是True')
else:
    print('b2是False')

b3 = (144%51==0)|(144%6==0)or(144%5==0)
if b3:
    print('b3是True')
else:
    print('b3是False')

#数值类型:0是假,非0是真:
n = 0
if n:
    print('n不是零值')
else:
    print('n是零值')

#字符串类型:空值是假,非空是真:
s = ""
if s:
    print('s不是空字符串')
else:
    print('s是空字符串')

#元组类型,非空是真:
t = ()
if t:
    print('t不是元组')
else:
    print('t是空元组')

#列表类型,空值是假,非空是真:
l = []
if l:
    print('l不是空列表')
else:
    print('l是空列表')

#集合类型,空值是假,非空是真:
d = {}
if d:
    print('d不是空集合')
else:
    print('d是空集合')

#函数类型,返回值=0也视作空:
def func():
    print("函数被调用")
    return 0
if func():
    print('func()返回值不是空')
else:
    print('func()返回值为空')

#单行用法:
x=input("dog? pig? cat?")
v="Yes" if x=="pig" else "no"
print(v)

