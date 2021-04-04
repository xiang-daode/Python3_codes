# 在这里写上你的代码 :-)
'''
题目026：利用递归方法求5!。
'''
def fac(x):
    if x>1:
        return x*fac(x-1)
    else:
        return x

def tm026():
    '''
    【个人备注】：按题目要求，公式f(n)=n*f(n-1)，递归调用求解。
    '''
    print(fac(5))

tm026()
