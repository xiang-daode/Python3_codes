#三位数各位数立方和相加等于其本身
#法1
a=range(100,1000,1)
for m in a:
    b0=str(m)[0] #str参数数字转字符串
    b1=str(m)[1]
    b2=str(m)[2]
    if int(b0)**3+int(b1)**3+int(b2)**3==m: #int字符串转数字
        print(m)
#法2
for x in range(100,1000，1):
    low=x%10 #作商取余
    high=x//100 #取整商
    middle=(x//10)%10
    sum=low**3+high**3+middle**3 #pow(low,3)+pow(high,3)+pow(middle,3)
    if sum==x:
        print(x,end=' ')
