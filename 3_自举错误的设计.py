# 自举错误的设计:
v=float(input('请输入一个正数:'))

if v<0:
    raise ValueError('不能是负数')
elif v==0:
    raise ValueError('0也不能用')
else:
    print(f"{v}的平方是{v*v},{v}的平方根是{v**0.5}")
