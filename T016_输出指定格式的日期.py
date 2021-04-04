# 在这里写上你的代码 :-)
'''
题目016：输出指定格式的日期。
'''
def tm016():
    '''
    【备注】：常用的日期时间方法
    '''
    import time
    print(time.time()) # 时间戳 1498539133.655
    s0=str(time.time())
    s1=s0.split('.')
    print(s1[0],s1[1]) #s1[1]可用于作随机数
    print(chr(0x4e00+int(s1[1])%20902)) #随机的汉字
    print(time.localtime())                                     # 时间元组 tm_year=2017, tm_mon=6, tm_mday=27, tm_hour=12, tm_min=53, tm_sec=16, tm_wday=1, tm_yday=178, tm_isdst=0
    print(time.asctime())                                       # 时间的一种可读文本形式 'Tue Jun 27 12:53:50 2017'
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))  # 按指定文本格式输出时间 '2017-06-27 13:00:57'

    st = time.localtime(time.time())                            # 时间戳 转化成 时间元祖
    st = time.strptime('2018/1/23','%Y/%m/%d')                  # 时间文本 转化成 时间元祖
    date = time.strftime('%Y-%m-%d',st)                         # 时间元祖 转化成 时间文本  '%Y-%m-%d %H:%M:%S'
    print(date)                                                 # 前面两条函数配合着用，相当于将时间文本重新格式化。

tm016()
