# 推导式返回新列表:

myList=[1,2,3,4,5,6,7,8,9]
a=[3*x for x in myList]  #使用表达式处理全部元素时用
print(a)

#当无else时,if句放在末尾:
b=[3*x for x in myList if x>5 ]
print(b)

#当有else时,先写出"10*x if x>5 else x/10",再写出"for x in myList"
b=[10*x if x>5 else x/10 for x in myList]
print(b)

#本质上是三目表达式在先,遍历在后. ---可以这样来记住:
b=[(10*x if x>5 else x/10) for x in myList]
print(b)
