import math

def zero(n):
    num = 0

    while True:
        n = int(n / 5)
        if n == 0:
            break
        num = num + n

    return num

print(zero(10000))