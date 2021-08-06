# 字典(dict),添加元素("键-值"对)
A={'fox':33,'dog':44,'bee':11}
A['pig']=77
A['cow']=99
print(A)

#按值(数字)排序:
B=sorted(A,key= lambda x:x[1])
print(B)

#按键(字母)排序:
C=sorted(A,key= lambda x:x[0])
print(C)

# 根据key的升序排列，把(key,value)都打印出来
D = sorted(A.items(), key=lambda d: d[0], reverse=False)
print(D)

# 根据value的降序排列，把(key,value)都打印出来
E = sorted(A.items(), key=lambda d: d[1], reverse=True)
print(E)

# 筛选出"值>40"的元素:
print('筛选出"值>40"的元素:')
for d in E:
    if d[1]>40:
        print(d)


# 筛选出"值在(x>22 且 x<99)区间"的元素:
F=list(filter(lambda x: x[1]>22 and x[1]<99,E))
print("值在(x>22 且 x<99)区间中:\n",F)


