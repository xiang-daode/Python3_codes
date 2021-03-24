import math

s= input("一元二次方程的三个系数（a*xx+b*x+c）英文输入法下输入a,b,c并回车 :  ")
sa=s.split(',')
if len(sa)!=3:
  print('数据无效！')
  exit

print(sa)
a=float(sa[0])
b=float(sa[1])
c=float(sa[2])
 
a2=2*a
dlt=b*b-4*a*c
if a!=0 and dlt>=0:
    x1=(-b-math.sqrt(dlt))/a2
    x2=(-b+math.sqrt(dlt))/a2
    print("x1=",x1,",  x2=",x2)
    
if a!=0 and dlt<0:
    im=math.sqrt(-dlt)
    m2=abs(im/a2)
    x1=str(-b/a2)+'-'+str(m2)+'i'
    x2=str(-b/a2)+'+'+str(m2)+'i'
    print("x1=",x1,",  x2=",x2)
