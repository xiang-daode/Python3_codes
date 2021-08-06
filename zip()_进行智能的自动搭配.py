# zip()函数:能够进行智能的自动搭配:

print(list(zip('ABCD','6789')))
print(list(zip(['fox','cat','dog'],[11,22,33])))

q = ['姓名', '年龄', '爱好']
a = ['狐狸1', '5', '鸡肉']
for q, a in zip(q, a):
     print('{0}  {1} '.format(q, a))


q = ['姓名', '年龄', '爱好']
a = [['狐狸1', '狐狸2', '狐狸3'],['11', '22', '33'],['犲肉', '兔肉', '鸡肉']]
for q, a in zip(q, a):
     print('{0}  {1} '.format(q, a))
