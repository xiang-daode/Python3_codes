# 在这里写上你的代码 :-)
import random

x=random.random()
print(x)
print(20802*x+19968)

#生成汉字:
h=int(20802*x+19968)
print(chr(h))


#生成汉字:
h=random.randint(0x4e00,0x5fa9)
print(chr(h))


