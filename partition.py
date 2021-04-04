# 能找到的情形:
a='1234abcd789xyz'
b='cd78'
x=a.partition(b)
print(x[0]) # 1234ab
print(x[1]) # cd78
print(x[2]) # 9xyz
print(x) # ('1234ab', 'cd78', '9xyz')

# 不能找到的情形:
c='78cd'
x=a.partition(c)
print(x[0]) # 1234abcd789xyz
print(x[1]) #
print(x[2]) #
print(x) # ('1234abcd789xyz', '', '')

