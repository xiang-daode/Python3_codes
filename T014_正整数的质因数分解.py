# 在这里写上你的代码 :-)
'''
题目014：将一个正整数分解质因数(如手机号,身份证号)。例如：输入90,打印出90=2*3*3*5。
'''
def tm014():
    '''
    【备注】：拆到因数2为止，如输入一个整数(手机号):13058943056。
    分解结果:[2, 2, 2, 2, 53, 257, 59921]
    '''
    import math
    num = int(input('输入一个整数:'))
    arr = []
    while num>1:
        for i in range(2,int(math.sqrt(num))+1): # 因为题目是一个没写范围正整数，开方可以有效减少该值过大时候的计算量
            if num%i==0:
                arr.append(i)
                num = num//i
                break
        else:
            arr.append(num)
            break
    print(arr)

tm014()
