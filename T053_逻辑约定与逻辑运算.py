# 在这里写上你的代码 :-)
'''
题目053_逻辑约定与逻辑运算
按位与 &
按位或 |
按位异或 ^
按位取反 ~
'''
def tm053():
    '''
    【个人备注】：
    '''
    x = False #在位运算中作0
    y = True  #在位运算中作1
    print(int(x),int(y)) #0,1
    print(x, y,not x,not y) # False True True False
    #
    print(x & y)         # False
    print(x | y)         # True
    print(x - y)         # -1
    print(x ^ y)         # True
    print(~x,~y,~9)      # -1 -2 -10 ,即用-1减去原数:-1-0=-1,-1-1=-2,-1-9=-10

    #注意空值为假,空元素的集合\列表\元组也是假," "或' '内容是space,作真:
    print(bool(5>3),bool(''),bool(" "),bool([]),bool(()),bool({}))#True False True False False False
tm053()
