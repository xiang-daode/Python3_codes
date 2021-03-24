# 1~9999包含2个8的数字有几个
sum=0
for i in range(1, 10000):
    num = len(str(i))
    if (num == 2):
        a = i // 10
        b = i % 10
        if (a==8 and b==8):sum=sum+1
    elif (num == 3):
        a = i // 100
        b = (i - a * 100) // 10
        c = i % 10
        if(a==b==8 or a==c==8 or b==c==8):sum=sum+1
    else:
        a = i // 1000
        b = (i - a * 1000) // 100
        c = (i - a * 1000 - b * 100) // 10
        d = i % 10
        if (a == b == 8 or a == c == 8 or a==d==8 or b == c == 8 or b==d==8 or c==d==8): sum = sum + 1

print(sum)