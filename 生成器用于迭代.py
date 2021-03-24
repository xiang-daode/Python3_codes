
#用于字符串反向:
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('11*9=99'):
    print(char,end=' ')


#用数组的各元素进行处理:
def fun(data):
    for x in data:
        yield x*x

print()
for v in fun([1,3,5,7,9]):
    print(v,end=' ')
