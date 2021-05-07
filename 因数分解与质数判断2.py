
# isPrime ?---素数(质数)判断
def isPrime(x):
    prime=True
    for i in range(2,x-1):
        if x%i==0:
            prime=False
    return prime

#100---999(包含999)内的所有质数:
for i in range(100,1000):
    if isPrime(i):
        print(i,end=',')
