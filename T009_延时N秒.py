# 在这里写上你的代码 :-)
'''
题目009：暂停一秒输出。
'''
def tm009():
    '''
    【备注】：time.sleep()，用过的都知道。
    '''
    import time
    a = time.time()
    time.sleep(1)
    b = time.time()
    print(a,b,"时间差=",b-a)

print(tm009())
