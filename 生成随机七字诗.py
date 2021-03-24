# 在这里写上你的代码 :-)
import random

#x=random.random()
#print(x)
#print(20802*x+19968)

#生成汉字:
#h=int(20802*x+19968)
#print(chr(h))
print("========= 天下大事预测诗 ==========")
for i in range(8):
    for j in range(7):
        x=random.random()
        h=int(20802*x+19968)
        print(chr(h),end='')
    print(';')
print("========= 项道德 撰 ==========")
