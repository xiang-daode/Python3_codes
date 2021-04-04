# 复数的一般运算
# 复数的赋值:
a=3+4j #复数1
b=3-4j #复数2
#用以下二行也等效:
a=complex(3,4)#复数1
b=complex(3,-4)#复数2
# 一些简易运算:
print(a+b) #复数加法
print(a-b) #复数减法
print(a*b) #复数乘法
print(a/b) #复数除法
print(a*a+b*b) #复数混合运算
print(a**2+b**2)#复数混合运算
print((a+b)*(a-b))#复数混合运算
'''返回结果:
(6+0j)
8j
(25+0j)
(-0.28+0.96j)
(-14+0j)
(-14+0j)
48j
'''
#在分形算法中,对平面区域中的点(x+jy)进行N次迭代,配合RGB出图,能出现奇妙的图案:
z=0.6-0.8j
c=.3+.4j
for i in range(10):
    z=z*z+c
    print(z)




