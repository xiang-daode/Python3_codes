# 在这里写上你的代码 :-)
a=[(3,6),(4,5),(1,8),(2,7)]
b0=sorted(a,key=lambda a:a[0],reverse=True)
b1=sorted(a,key=lambda a:a[1])
print(b0,'按第一关键字,倒序')
print('按第二关键字,从小到大',b1)
