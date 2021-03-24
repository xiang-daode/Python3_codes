# 在这里写上你的代码 :-)
lst = [1, 2, 3, 4, 5]
res = []
for i in lst:
  a = i*i
  res.append(a)

# 等价于下行:
res = list(map(lambda x:x*x, lst))
print(res)
