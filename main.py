#自定义函数-1：传入字符串作形参,直接打印,没有返回值：
def myFun(name):
    print(f'Hi, {name}')
#自定义函数-2：传入二个数字作形参,直接打印,没有返回值：
def myFun2(a,b):
    print(f'{a}+{b}={a+b}')

#自定义函数-3：传入字符串作形参,返回值是字符串：
def myFunB(name):
    return (f'Hi, {name}')

#自定义函数-4：传入二个数字作形参,计算后返回结果：
def myFun2B(a,b):
    return (f'{a}+{b}={a+b}')

if __name__ == '__main__':
    myFun('张大仙')
    myFun2(21,31)
    a=myFunB('李大侠')
    b=myFun2B(12,13)
    print(a,b)


