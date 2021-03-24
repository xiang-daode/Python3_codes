# 求(x,y)的最小公倍数:
def gbs(x,y):
    if x>y:
        z=y
    else:
        z=x
    f=1
    for i in range(z,2,-1):
        if(x%i==0 and y%i==0):
            f=f*i
            x=x/i
            y=y/i
    f=f*x*y
    return f;

v=gbs(18,12)
print(v)
