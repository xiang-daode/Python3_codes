# 在这里写上你的代码 :-)
'''
题目094：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
'''
def tm094():
    import time,random
    print('《猜大小0-1000之间》')
    x = random.randint(0,10)
    flag = input('是否开始(y/n)：')
    if flag=='y':
        s = time.time()
        while 1:
            m = int(input('请输入数字：'))
            if m>x:
                print('大了')
            elif m<x:
                print('小了')
            else:
                print('bingo!')
                break
        e = time.time()
        print('耗时%.2f秒'%(e-s))
        print(time.sleep(5))

tm094()
