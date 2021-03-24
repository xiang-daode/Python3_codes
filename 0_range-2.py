#range与list:
a=range(5)
print(list(a))

#按下标读取:
a=range(2,20,2)
print(a[0],a[1],a[2],a[len(a)-1])

#步长是负数:
a=range(100,80,-2)
print(list(a))

#转为元组tuple:
a=range(1,5)
print(tuple(a),a[0],a[1],a[2],a[len(a)-1])

#转为集合set:
a=range(1,11,2)
print(set(a),a[0],a[1],a[2],a[len(a)-1])


