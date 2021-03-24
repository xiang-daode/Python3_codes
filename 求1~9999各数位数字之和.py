# 1~9999各数位数字之和

for i in range(1, 9999):
    num = len(str(i))
    if (num == 1):
        sum=i
        print(sum)
    elif (num == 2):
        a = i // 10
        b = i % 10
        sum=a+b
        print(sum)
    elif (num == 3):
        a = i // 100
        b = (i - a * 100) // 10
        c = i % 10
        sum=a+b+c
        print(sum)
    else:
        a = i // 1000
        b = (i - a * 1000) // 100
        c = (i - a * 1000 - b * 100) // 10
        d = i % 10
        sum=a+b+c
        print(sum)
