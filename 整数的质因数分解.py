#整数的质因数分解_来自_Master\maths\prime_factors.py:

from __future__ import annotations

def prime_factors(n: int) -> list[int]:

    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    lt=prime_factors(2021) #质因数分解:分解年份
    print(lt)

    lt=prime_factors(13058943056) #质因数分解:分解手机号
    print(lt)

    lt=prime_factors(330523196001100018) #质因数分解:分解身份证号
    print(lt)
    
