# 在这里写上你的代码 :-)
'''
题目096：计算字符串中子串出现的次数。
'''
def tm096():
    '''
    【个人备注】：用count就行了
    '''
    x = 'ab,ab,aab,b,aaa'
    print(x.count(','))

    s=0
    for i in range(1,10000):
       s+=str(i).count('0')
    print('1,2,3,...9999中0出现了:',s)

    s=0
    for i in range(1,10000):
       s+=str(i).count('8')
    print('1,2,3,...9999中8出现了:',s)

tm096()
