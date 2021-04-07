# 列表元素的添加与插入:
lt=['bug','dog','pig']
lt.insert(0,'bee')
lt.append('fox')
print(lt)

#出栈(从右边弹出)
f=lt.pop()
print(f,lt)

#出栈(从左边弹出)
f=lt.pop(0)
print(f,lt)

