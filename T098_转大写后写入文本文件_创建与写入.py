# 在这里写上你的代码 :-)
'''
题目098：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
'''
def tm098():
    '''
    【个人备注】：字符串大写
    '''
    c = input()
    c = c.upper()
    with open('testT097.txt','w+') as f:f.write(c)

tm098()
