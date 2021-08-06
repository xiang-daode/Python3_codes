# list_列表(快速赋值)

#1,按运算符生成列表:
squares = []
for x in range(10):
     squares.append(x**2)
print(squares)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#2,按运算符生成列表:
squares = list(map(lambda x: x**2, range(10)))
print(squares)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#3,按运算符生成列表:
squares = [x**2 for x in range(10)]
print(squares)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#4,按运算符重新生成:
vec = [-4, -2, 0, 2, 4]
z= [x*2 for x in vec]  #[-8, -4, 0, 4, 8]

#5,按范围筛选:
vec = [-4, -2, 0, 2, 4]
z=[x for x in vec if x >= 0]    #[0, 2, 4]

#6,按[a,b]范围筛选:
vec = [-4, -2, 0, 2, 4]
z=[x for x in vec if x >= -3 and x<=3]    #[-2, 0, 2]

#7,对各元素使用内置函数删除前后空格:
F = ['  fox', '  cow ', 'bee  ']
z= [w.strip() for w in F]
print(z) #['fox', 'cow', 'bee']

#8:
from math import pi
z=[str(round(pi, i)) for i in range(1, 6)]
print(z) #['3.1', '3.14', '3.142', '3.1416', '3.14159']

#10,二维化为一维:
vec = [[1,2,3], [4,5,6], [7,8,9]]
z= [num for elem in vec for num in elem]
print(z)  #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#11,生成二维数据:
z=[(x, x**2) for x in range(6)]
print(z)  #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#12,生成二维数据:
z = []
for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             z.append((x, y))
print(z)  #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


#13,生成二维数据:
z=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(z)  #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

#14,使用双层FOR实现转置:
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
z=[[row[i] for row in matrix] for i in range(4)]
print(z)  #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#15,使用内置函数实现转置:
z=list(zip(*matrix))
print(z)  #[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]



