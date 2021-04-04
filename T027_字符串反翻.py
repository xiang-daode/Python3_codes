# 在这里写上你的代码 :-)
'''
题目027：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
用内置函数时: list(reversed('12345'))
理简便用: '12345'[::-1]
'''
def output(s,l):
    if l==0:
       return
    if l>0:
        print (s[l-1],end='')
        output(s,l-1)

def tm027():
    s = input('Input a string:')
    l = len(s)
    output(s,l)

tm027()
print('\n',list(reversed('12345')))
print('\n','12345'[::-1])

