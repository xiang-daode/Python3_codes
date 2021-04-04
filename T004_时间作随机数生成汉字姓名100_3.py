# 在这里写上你的代码 :-)
'''
题目004：时间函数妙用
'''
def tm004(x=[]):

    import time
    for i in range(100):

        v=19968+int(0xFFFF00*time.time() % 20902)
        time.sleep(0.00000001) #如delay()延时n秒
        w=19968+int(0xFF00FF*time.time() % 20902)
        x.append(['项'+chr(v)+chr(w)])

    return x

print(tm004())


