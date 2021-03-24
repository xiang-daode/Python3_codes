# 在这里写上你的代码 :-)

# 打包与解包:
a = ("Bill", "Steve", "Elon")
b = ("Gates", "Jobs", "Musk")

x = zip(a, b)

print(x)
print(list(x))
print(list(zip((77,88))))
print(list(zip((77,88))))
print(list(zip(*zip((77,88)))))
print(list(zip(*zip((77,88))))==[(77,88)])


## *zip()函数
print('=*'*10 + "*zip()函数" + '=*'*10)
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
print("*zip(m, n)返回:\n", *zip(m, n))
m2, n2 = zip(*zip(m, n))
# 若相等，返回True；说明*zip为zip的逆过程
print(m == list(m2) and n == list(n2))
