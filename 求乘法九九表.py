# 打印九九乘法表

for i in range(1,10):
    for j in range (1,i+1):
        print('%d*%d=%-3d' % (i, j, i * j), end='\t')
    print()