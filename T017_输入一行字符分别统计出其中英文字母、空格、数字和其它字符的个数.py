# 在这里写上你的代码 :-)
'''
题目017：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
def tm017():
    '''
    【备注】：笨一些的方法是:
    import string
    if c in string.ascii_letters: # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    if c == ' ':                  # 空格
    if c in string.digits:        # 0123456789
    更高级的方法是用正则

    以下使用专用函数(参见: https://www.runoob.com/python/python-strings.html)
    '''
    s = input('input a string:\n')
    letters,space,digit,others = 0,0,0,0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))


tm017()
