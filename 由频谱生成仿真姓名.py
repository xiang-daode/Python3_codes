# 在这里写上你的代码 :-)
import random


fx="姓氏频谱.txt"
fnm="名字频谱.txt"

#读取"姓氏频谱.txt"文件:
with open(fx, "r",-1,"GBK") as f:
    xs=f.read()
    xLen=len(xs)

#读取"名字频谱.txt"文件:
with open(fnm, "r",-1,"GBK") as f:
    mz=f.read()
    mLen=len(mz)

for i in range(600):
    r1=random.randint(0,xLen-1)
    r2=random.randint(0,mLen-1)
    r3=random.randint(0,mLen-1)
    print(xs[r1]+mz[r2]+mz[r3],end='\t')






