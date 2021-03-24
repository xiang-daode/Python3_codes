# 在这里写上你的代码 :-)
import random


fx="英汉2000单词.txt"

dic=[]
#读取文件:
with open(fx, "r",-1,"UTF-8") as f:
    xs=f.read()
    dic=xs.split('\n')
    xLen=len(dic)
    print("字典单词总行数:",xLen)

for i in range(4):
    ri=random.randint(0,xLen-1)
    print(dic[ri])





