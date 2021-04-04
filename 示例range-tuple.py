# range:
a=range(5) # 默认从0开始,在5以内,到不了5
print(a) # range(0, 5)

# range与tuple:
a=range(5) # 默认从0开始,在5以内,到不了5
print(tuple(a)) # (0, 1, 2, 3, 4)

a=range(1,5) #给出起点,终点(到不了的)
print(tuple(a)) # (1, 2, 3, 4)

a=range(1,11,2) #  给出起点,终点(到不了的),步长(正整数,负整数)
print(tuple(a)) # (1, 3, 5, 7, 9)

a=range(2,2468,2) # 最大下标这样获得:len(a)-1
print(len(a)) #元素数目:1233
print(a[0],a[1],a[2],a[len(a)-1]) #  2 4 6 2466

a=range(100,80,-2) # 前大后小的,步长应该是负数
print(tuple(a)) # (100, 98, 96, 94, 92, 90, 88, 86, 84, 82)

x,y,z='111',111*2,999/3 #元组可以一并赋值的
print(x,y,z) # 111 222 333.0


