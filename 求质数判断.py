#!/usr/bin/python
# -*- coding: cp936 -*-

from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
b=is_prime(361)
print(b)
b=is_prime(71)
print(b)
