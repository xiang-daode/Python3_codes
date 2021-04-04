# 1~9999各数位数字之和
sAll=0
for i in range(1, 9999+1):
    ln = len(str(i))
    lt = list(str(i))
    sum=0
    for m in lt:
        sum+=int(m)
    #print(sum,end=',')
    sAll+=sum
print(sAll)
