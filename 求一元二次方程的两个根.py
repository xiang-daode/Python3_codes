# 输出一元二次方程的两个根

def fc(a,b,c):
    x1=(-b+(b*b-4*a*c)**0.5)/(2*a)
    x2 = (-b - (b * b - 4 * a * c) ** 0.5) / (2 * a)
    print(x1,x2)

a=int(input())
b=int(input())
c=int(input())
fc(a,b,c)