# 在这里写上你的代码 :-)
x=filter(lambda v: v % 2==0,[1,2,3,4,5,6,7,8,9])
print(list(x))

x=filter(lambda v: v % 3==0,(1,2,3,4,5,6,7,8,9))
print(list(x))

x=filter(lambda v: v % 5==0,{1,2,3,4,5,6,7,8,9})
print(list(x))
