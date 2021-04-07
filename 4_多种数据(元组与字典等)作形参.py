# 多种数据作形参:
def fun(s1,*args,**kv):
    print(s1)
    for m in args:
        print(m)
    for k in kv:
        print(k,"=",kv[k])
#函数的调用:
fun('A cat says :', #第一个参数传入到s1
'miao,','miao--,','wao,','wao--!', #多余的,可视作元组数据的传入到*args
hm=88, #多余的,'键-值'对数据的传入到 **kv
nm='dog', #多余的,'键-值'对数据的传入到 **kv
age=12 #多余的,'键-值'对数据的传入到 **kv
)

