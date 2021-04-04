# 在这里写上你的代码 :-)
'''
题目010：暂停一秒输出，并格式化当前时间。
'''
def tm010():
    '''
    【备注】：时间格式化。关于时间处理的更多内容可以看tm016。
    '''
    import time
    f=time.time()
    print(f,(f-int(f))) #1616673949.845809 0.8458089828491211
    s=str(f-int(f))[2:] #丢弃前二字符
    print(s,int(s,10)) #可用于大随机数:8458089828491211 8458089828491211

    #年月日 时分秒 格式的输出:
    a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) # time.localtime()时间戳转化成时间元组
    print(a)
    time.sleep(1)
    b = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) # time.strftime()时间元组转化成时间文本
    print(b)

print(tm010())
