# 1~9999所有质数
for i in range(2,10000):
    f = 0
    for j in range(2,i):
        if i%j==0:
            f=1
            break;
    if f==0:
        print(i)


