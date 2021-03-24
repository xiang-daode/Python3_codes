# 在这里写上你的代码 :-)
from random import randint
#
for m in [1,2,3,4,5,6,7]:
    print(m,end=' ')

for m in "1234567":
    print(m,end='.')

for m in "0123456789":
    print(hex(ord(m)),end='\n')

for m in iter("1234567"):
    print(m,end='_')

# 自定义函数,作猜数的返回结果
def guess():
   return randint(0, 10)
#-------End def--------
num = 1 #记次数
# 数为5时中断跳出:
for i in iter(guess, 5):
   print("第%s次猜测，猜测数字为: %s" % (num, i))
   num += 1
# 当 guess 返回的是 5 时，会抛出异常 StopIteration，但 for 循环会处理异常，即会结束循环
