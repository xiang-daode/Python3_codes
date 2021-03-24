import numpy as np


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
f1=  lambda x: x % 3 == 0
print(f1(foo[3]))

f2=  lambda x: x // 10
print(f2(foo[3]))

f1=  lambda x: x >>2
print(f1(foo[5]))
