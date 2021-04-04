# 在这里写上你的代码 :-)
'''
题目097：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
'''
def tm097():
    '''
    【备注】：保存文件的方法，记住即可。
    with .. as ..打开会自动关闭。
    其他方式打开，别忘了通过代码关闭。
    '''
    path = 'testT097.txt'
    with open(path,'w+') as f:f.write('')
    while 1:
        c = input()
        if c=='#':
            break
        else:
            with open(path,'a+') as f:f.write(c)

tm097()
