# 在这里写上你的代码 :-)
def fun():
    '''这是文档的多行注释
    测试计算: 64+36
    ----By daode1212
    '''
    v=64+36
    return "64+36="+str(v)


print(fun.__doc__)
print(fun())
