# 在这里写上你的代码 :-)
'''
题目042：局部变量、全局变量,学习使用auto定义变量的用法。
'''
def tm042():
    '''
    【备注】：变量作用域, python是有分局部变量、全局变量的等区分的。
     在函数内部定义与赋值的变量,在本函数被调用时,每次都初始化了:
    '''
    num = 2 #全局变量,可在程序运行中被修改
    def autofunc():
        num = 1 #内部定义与赋值的变量,每次都初始化
        print('internal block num = %d'%num)
        num += 1

    for i in range(3):
        print('The num = %d'%num) #读取全局变量
        num += 1 #修改全局变量
        autofunc()


tm042()
'''
以上实例输出结果为：
The num = 2
internal block num = 1
The num = 3
internal block num = 1
The num = 4
internal block num = 1
'''
