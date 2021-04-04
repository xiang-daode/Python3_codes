# 在这里写上你的代码 :-)
'''
题目070：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
'''
def tm070():
    '''
    【个人备注】：简单
    '''
    def getlength(string):
        return len(string)
        '''
        if __name__ == '__main__':
            x = 'abcde12345'
            print(getlength(x))
        '''
    # 这样调用也行:
    print(getlength('12345abcde'))

tm070()
