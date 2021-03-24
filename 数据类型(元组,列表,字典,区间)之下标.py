# 在这里写上你的代码 :-)

# 字符串下标[从0开始]
tup0 = "学习编程真好0123456789"
print(tup0[4],tup0[10])

# 将字符串转换成元组下标[从0开始]
tup1 = tuple("hello")
print(tup1[0])

# 将列表转换成元组下标[从0开始]
list1 = ['Python', 'Java', 'C++', 'JavaScript']
tup2 = tuple(list1)
print(tup2[2])

# 将字典转换成元组下标[从0开始,负数则从右数起]
dict1 = {'a' : 100, 'b' : 42, 'c' : 9}
tup3 = tuple(dict1)
print(tup3[-3])

# 将区间转换成元组下标[从0开始]
range1 = range(1, 6)
tup4 = tuple(range1)
print(tup4[4])
