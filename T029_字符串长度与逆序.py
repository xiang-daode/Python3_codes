# 在这里写上你的代码 :-)
'''
题目029：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
def tm029():
    '''
    【备注】：
    list倒序可以用list.reverse()；
    字符串用步长=-1的方式来倒序最为简洁。
    '''
    num = 12345
    s = str(num)
    print(len(s))
    print(s[::-1])

tm029()
