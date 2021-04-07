# 元组数据作为函数的形参:
#传入是字符串时:
def fun(*args,sep='#'):
    print(sep.join(args))

#调用:
fun('1','2','3','4')
fun('1','2','3','4',sep='@')
fun('1','2','3','4',sep='&')

#传入是数值时:
def fun2(*args):
    L=[]
    for m in args:
        L.append(m)
    print(L)
#调用:
fun2(5,4,3,2,1)



