# 在这里写上你的代码 :-)
'''
题目001：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
类同于,从四张卡片中抽出3张的所有排列情形
'''


def tm001():
    '''
    【个人备注】：穷举法,修改:项道德
    '''
    arr = []
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i!=j and j!=k and i!=k: # 互不相同且无重复数字的三位数, 原有这一判断可略去: and num not in arr
                    num = 100*i+10*j+k
                    arr.append(num)
    print(len(arr),arr)

tm001()
