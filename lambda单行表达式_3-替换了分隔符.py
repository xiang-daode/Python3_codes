import numpy as np


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]


s0="2, 18, 9, 22, 17, 24, 8, 12, 27"
Func = lambda s: "_".join(s.split(', '))
print(Func(s0)) #替换了分隔符
