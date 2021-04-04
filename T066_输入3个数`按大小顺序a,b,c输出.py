# 在这里写上你的代码 :-)
'''
题目066：输入3个数`按大小顺序a,b,c输出。
'''
def tm066():
    arr=[]
    for i in range(3):
        a = input('请输入数字:')
        arr.append(int(a))
    arr.sort(reverse=True)
    print('从大到小',arr)

tm066()
