# 在这里写上你的代码 :-)
'''
题目004：输入某年某月某日`判断这一天是这一年的第几天
'''
def tm004():
    '''
    【个人备注】：知道python有时间元组这一概念，这道题完全不需要计算。
    时间元组包含九个属性
    tm_year     年
    tm_mon      月(1~12)
    tm_mday     日(1~31)
    tm_hour     时(0~23)
    tm_min      分(0~59)
    tm_sec      秒(0~61, 60或61是闰秒)
    tm_wday     星期(0~6, 0是周一)
    tm_yday     第几天(1~366, 366是闰年)
    tm_isdst    夏令时(1夏令时、0非夏令时、-1代表未知。平时写代码基本用不到。夏时令是指部分国家地区，夏季人为将时间调快一小时，早睡早起，以便充分利用夏日光照，节约用电。中国从1992年起就没有再执行过这个了)
    '''
    import time
    #print(time.ctime()) #Thu Mar 25 15:54:07 2021
    #print(time.asctime()) #Thu Mar 25 15:54:32 2021
    print(time.time()) #1616658958.8134286---可用作随机数
    time.sleep(0.00001) #如delay()延时n秒

    print(time.time())
    date = input('输入时间(例如2018-01-23):')
    st = time.strptime(date,'%Y-%m-%d') # 时间文本转化成时间元祖
    num = st.tm_yday
    print(num)

tm004()


