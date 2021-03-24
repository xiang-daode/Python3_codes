# 打印1~100各数中3,5,7的倍数（且）

for i in range(1,101):
    if(i%3==0 and i%5==0 and i%7==0):
        print(i)