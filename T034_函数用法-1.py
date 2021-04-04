# 在这里写上你的代码 :-)
'''
题目034：练习函数调用。
'''
def tm034_1():
    '''
    【备注】：没有本质内容时,可以放入"pass",返回值是:None。
    '''
    pass


def tm034_2():
    '''
    【备注】：返回值可以是"True"或"False"。
    '''
    return True

def tm034_3(x,L=[]):
    '''
    【备注】：注意在每次调用函数时,L内容在增加中。
    '''
    L.append(x)
    print(L)
    return 'OK !'

L=[]
print(tm034_1())
print(tm034_2())
print(tm034_3(1)) #不传入L
print(tm034_3(2)) #不传入L
print(tm034_3(3)) #不传入L
print(tm034_3(71,L))
print(tm034_3(72,L))
print(tm034_3(73,L))
print(L)

