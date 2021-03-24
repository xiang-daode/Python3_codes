# 求1~9999的均值，标准差
sum=0
for i in range(1,10000):
    sum=sum+i
avg=sum/9999
print(avg)
sum=0
for i in range(1,10000):
    sum=sum+(i-avg)*(i-avg)
s=(sum/9998)**0.5
print(s)