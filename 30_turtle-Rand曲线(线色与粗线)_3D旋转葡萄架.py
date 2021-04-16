from turtle import *
import random as rnd
import math

Lm=[] #枝条集合
Li=[] #单一枝条

tracer(False)  # 快速(不用小乌龟)
ht()  # 隐藏小乌龟

#===========================================
#单一枝条:
def gen(x0,y0,z0,lf):
    (r,g,b)=(rnd.random()/7,rnd.random(),rnd.random()/3)
    u=2*rnd.random()-1 +3.1416/2
    v=2*rnd.random()-1
    k2=4*lf
    x=x0+k2*math.cos(u)*math.cos(v)
    y=y0+k2*math.sin(u)*math.cos(v)
    z=z0+k2*math.sin(v)
    Li.append([x,y,z,r,g,b,lf])
    lf-=1
    if lf>1:
        gen(x,y,z,lf)
    else:
        Lm.append(Li)

#===========================================
#生成主框架:
def main():
   while len(Li)<50:
         k=6+rnd.randint(1,len(Li)-7)
         (x,y,z,r,g,b,lf)=(Li[k][0],Li[k][1],Li[k][2],Li[k][3],Li[k][4],Li[k][5],Li[k][6])
         if lf>3:
             gen(x,y,z,lf)
             print(k)


#===========================================
#旋转与生成三维图像:
def mainRot(m):
    clear()
    for i in range(len(Lm)):
        pd()
        L1=Lm[i]
        #print(L1)
        for k in range(len(L1)):
            (x0,y0,z0)= (L1[k][0],L1[k][1],L1[k][2])
            (r,g,b)= (L1[k][3],L1[k][4],L1[k][5])
            lf= L1[k][6]
            pencolor(r,g,b)
            pensize(lf)

            '''
            # 绕Z旋转:
            x1 = x0 * math.cos(m / 97) - y0 * math.sin(m / 97)
            y1 = x0 * math.sin(m / 97) + y0 * math.cos(m / 97)
            z1 = z0
            '''
            # 绕Y旋转:
            x2 = x0 * math.cos(m / 37) + z0 * math.sin(m / 37)
            y2 = y0
            z2 = -x0 * math.sin(m / 37) + z0 * math.cos(m / 37)

            # 绕X旋转:
            x3 = x2
            y3 = y2 * math.cos(-0.15) - z2 * math.sin(-0.15)
            z3 = y2 * math.sin(-0.15) + z2 * math.cos(-0.15)

            #绘制:
            setx(x3);sety(y3);
            dot(4*lf)
            goto(x3, y3)
        pu()
    update()  # 更新画布
    m -= 3
    # 递归:
    if m > 0:
        ontimer(mainRot(m), 20)

#===============================
gen(0,-275,0,18) #初始化
main() #生成框架
mainRot(3000) # 生成3D图像

