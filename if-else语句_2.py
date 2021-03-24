# 在这里写上你的代码 :-)
#优化增加输入字符的判断以及异常输出:
import sys

k=5 #有限次数失败后,退出程序
while True:
    try:
        num=float(input('请输入一个数字：'))
        if num==0:
            print('输入的数字是零')
        elif num>0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
        break
    except ValueError:
        print('输入无效，需要输入一个数字,再继续下去...')
        k=k-1
        if(k<1):
            sys.exit()
