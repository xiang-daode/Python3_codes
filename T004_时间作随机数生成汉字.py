# 在这里写上你的代码 :-)
'''
题目004：时间函数妙用
'''
def tm004():
    x=[]
    import time
    for i in range(100):
        time.sleep(0.000001) #如delay()延时n秒
        v=19968+int(0xFFFFFF*time.time() % 20902)
        x.append([v,chr(v)])

    print(list(x))

tm004()


