# 在这里写上你的代码 :-)

'''
题目038：参差型数据[][],不同于二维数组,在AI中经常用到
'''
def tm038():
    '''
    【备注】：第一维用元素,第二维用下标
    '''

    s=''
    a = [[0,1,2,3],[.4,.5,.6],[70,80,90,100],['fox','hen']]
    for m in a: #
       for j in range(len(m)): #
           s+=' '+str(m[j])
       s+='\n'
    print(s)
tm038()
