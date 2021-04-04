# 在这里写上你的代码 :-)
'''
题目045：统计 1 到 100 之和。
'''
def tm045():
    '''
    【备注】：range(1,101)中第二个数是不到达的.
    可拓展到级数计算
    '''
    s = 0 #自然数,求和
    for i in range(1,101):
        s+=i
    print(s)

    s = 0 #自然数平方,求和
    for i in range(1,101):
        s+=i*i
    print(s)

    s = 0 #自然数开4次方,求和
    for i in range(1,101):
        s+=i**0.25
    print(s)

    s = 0 #欧拉数,e=2.7182818284590455...
    for i in range(1,101):
        fi=1 #计算阶乘
        for j in range(2,i):
           fi*=j
        s+=1/fi
    print(s)



    # 方法二,更简洁的方法:
    print(sum(range(1,101)))

tm045()
