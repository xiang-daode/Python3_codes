# 在这里写上你的代码 :-)
'''
题目041：模仿静态变量的用法。
'''
def tm041():
    '''
    【备注】：如果是函数中的局部变量，每次调用函数都会初始化。
    而类中的变量，创建类的时候初始化，每次执行类中的函数的时候，不会初始化类变量。
    可参考题目034：练习函数调用。
    '''
    def varfunc():
        var = 0
        print('var = %d' % var)
        var += 1
    if __name__ == '__main__':
        for i in range(3):
            varfunc()

    # StaticVar作为类的一个属性，相当于静态变量
    class Static:
        StaticVar = 5
        def varfunc(self):
            self.StaticVar += 1
            print(self.StaticVar)

    print(Static.StaticVar)
    a = Static()
    for i in range(3):
        a.varfunc()

tm041()
