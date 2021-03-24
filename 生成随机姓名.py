# 在这里写上你的代码 :-)
import random

x=random.random()
print(x)
print(20802*x+19968)

#生成汉字:
h=int(20802*x+19968)
print(chr(h))

for i in range(300):
    s1="项"
    x1=random.random()
    h1=int(20802*x1+19968)
    x2=random.random()
    h2=int(20802*x2+19968)
    print(s1+chr(h1)+chr(h2),end=',')

