# 1~9999各位数字和是24有哪些
for i in range(1, 9999):
    num = len(str(i))
    if (num == 3):
        a = i // 100
        b = (i - a * 100) // 10
        c = i % 10
        if a+b+c==24:
            print(i)
    else:
        a = i // 1000
        b = (i - a * 1000) // 100
        c = (i - a * 1000 - b * 100) // 10
        d = i % 10
        if a + b + c +d== 24:
            print(i)
