# 在这里写上你的代码 :-)
#生成器,generators:

#生成器也是一种函数,每一次调用,只会交出一个值:
def fun01(iterable):
    for i in iterable:
        yield i*i  #每一次只提供一个值

#在大量元素的搜索中,节约了空间与时间:
for j in  fun01(range(1,0xFFFFFFFFF)):
    print(j,end=';')
    if j>=100:
        break


