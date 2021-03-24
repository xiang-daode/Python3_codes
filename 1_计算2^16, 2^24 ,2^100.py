# 计算2^16 2^24 2^100

def pf(x):
    sum=2
    for i in range(1,x):
        sum=sum*2
    return sum

print(pf(16))
print(pf(24))
print(pf(100))