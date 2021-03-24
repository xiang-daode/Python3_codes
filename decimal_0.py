from decimal import *



v1=round(Decimal('0.70') * Decimal('1.05'), 2)
print('',v1)    #0.74
v2=round(.70 * 1.05, 2)
print('',v2)    #0.73

v3=Decimal('1.00') % Decimal('.10')
print('',v3)    #0.00
#1.00 % 0.10


v4=sum([Decimal('0.1')]*10) == Decimal('1.0')
print('',v4)    #True

v5=sum([0.1]*10) == 1.0
print('',v5)    #False


#decimal 模块提供了运算所需要的足够精度:
v6=getcontext().prec = 36
print('',v6)    #36


v7=Decimal(1) / Decimal(7)
print('',v7)    #0.142857142857142857142857142857142857

 
v8=Decimal(2) **100
print('',v8)

v9=Decimal(123456789) *Decimal(987654321)
print('',v9) 
