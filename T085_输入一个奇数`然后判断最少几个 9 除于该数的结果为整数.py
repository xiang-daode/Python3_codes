# 在这里写上你的代码 :-)
'''
题目085：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
'''
def tm085():
    '''
    【个人备注】：挨个试直到整除为止即可。
    '''
    x = int(input('input a number:'))
    for i in range(1,61):
        if int('9'*i)%x==0:
            print(i)
            break
    else:
        print('no way')

tm085()
