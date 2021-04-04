# 在这里写上你的代码 :-)
'''
题目078：找到年龄最大的人，并输出。
person = {"li":18,"wang":50,"zhang":20,"sun":22}
'''
def tm078():
    '''
    【个人备注】：官网的答案也基本一样。
    '''
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    name,age='',0
    for p in person.keys():
        if person.get(p)>age:
            name,age=p,person.get(p)
    print(name,age)

tm078()
