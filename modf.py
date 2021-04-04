# 在这里写上你的代码 :-)
import math
a=17/7
print(a) #原来的商
#math.modf(x):将x拆分为整数与小数两个数(符号与原来的一致)
b=math.modf(a)
print(b)
print(b[0],b[1])
a=-17/7
b=math.modf(a)
print(b)
print(b[0],b[1])
