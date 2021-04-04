# 在这里写上你的代码 :-)
'''
题目031：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''


def tm031():
    '''
    【备注】：注意下标应用的技巧
    '''
    week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    inp = ''
    while 1:
        arr = []
        inp = inp+input('请输入一个字母:')
        for day in week:                    # 挑出满足输入的星期
            if inp==day[:len(inp)]:
                arr.append(day)
        if len(arr)==1:                     # 只剩一个，说明唯一，可以输出结果
            print('以%s开头的单词是:%s'%(inp,arr[0]))
            inp=''
        elif len(arr)==0:                   # 一个都没有说明输错了，需要重新输入
            print('没有%s开头的单词'%inp)
            inp=''

tm031()
