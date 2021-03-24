# 在这里写上你的代码 :-)
def add(x,y):
    return x,y
list1 = [1,3,5]
list2 = [2,4,6,8]
a = list(map(add, list1, list2))
print(a)

def add2(x,y):
    return x+y
a = list(map(add2, list1, list2))
print(a)
