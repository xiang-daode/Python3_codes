# 在这里写上你的代码 :-)
'''
题目005：输入三个整数x,y,z，请把这三个数由小到大输出。
'''
def tm005():#三个数分开输入时:
    print('输入三个整数')
    x = int(input('输入第1个整数:'))
    y = int(input('输入第2个整数:'))
    z = int(input('输入第3个整数:'))
    l = [x,y,z]
    arr = sorted(l)  # 你也可以使用list.sort()方法来排序，此时list本身将被修改
    print(arr)

#tm005()

def tm005b(): #一次性全部输入三个数
    s=input('输入3个数,形如: 34,78,13:')
    a=s.split(',')  #拆开成list
    x=float(a[0])
    y=float(a[1])
    z=float(a[2])
    arr = sorted([x,y,z])
    print(arr)

tm005b()
