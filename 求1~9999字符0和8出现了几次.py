# 1~9999字符0和8出现了几次

zero = 0
eight = 0
for i in range(1, 9999):
    num = len(str(i))
    if (num == 1):
        if i == 0:
            zero = zero + 1
        elif i == 8:
            eight = eight + 1
    elif (num == 2):
        a = i // 10
        if a == 0:
            zero = zero + 1
        elif a == 8:
            eight = eight + 1
        b = i % 10
        if b == 0:
            zero = zero + 1
        elif b == 8:
            eight = eight + 1
    elif (num == 3):
        a = i // 100
        if a == 0:
            zero = zero + 1
        elif a == 8:
            eight = eight + 1
        b = (i - a * 100) // 10
        if b == 0:
            zero = zero + 1
        elif b == 8:
            eight = eight + 1
        c = i % 10
        if c == 0:
            zero = zero + 1
        elif c == 8:
            eight = eight + 1
    else:
        a = i // 1000
        if a == 0:
            zero = zero + 1
        elif a == 8:
            eight = eight + 1
        b = (i - a * 1000) // 100
        if b == 0:
            zero = zero + 1
        elif b == 8:
            eight = eight + 1
        c = (i - a * 1000 - b * 100) // 10
        if c == 0:
            zero = zero + 1
        elif c == 8:
            eight = eight + 1
        d = i % 10
        if d == 0:
            zero = zero + 1
        elif d == 8:
            eight = eight + 1
print(zero,eight)