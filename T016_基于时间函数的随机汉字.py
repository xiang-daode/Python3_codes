# 在这里写上你的代码 :-)
'''
题目016：输出指定格式的日期。
'''
import time

def tm016(r,c):
    '''
    【备注】：时间戳生成随机汉字诗方法
    '''

    #print(time.time()) # 时间戳 1498539133.655
    s0=str(time.time())
    s1=s0.split('.')
    #print(s1[0],s1[1]) #s1[1]可用于作随机数
    print(chr(0x4e00+((1234*r+7531*c)^int(s1[1]))%20902),end='') #随机的汉字
    #return  chr(0x4e00+((1234*r+7531*c)^int(s1[1]))%20902)


print('==== 世界预测诗 ====')
for row in range(8):
    for col in range(7):
       tm016(row,col)
    print()
print('\n项道德撰, ',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))  # 按指定文本格式输出时间 '2017-06-27 13:00:57'
