# 在这里写上你的代码 :-)

#定义单一变量的函数:
fun=lambda x:x**2+2*x+7
print(fun(1))# out:10

#定义一种二元的函数:
fun=lambda x,y:x+y
print(fun(4,6))# out:10

#定义一种新的异或运算:
fun=lambda x,y:(x-y)^(x+y)
print(fun(64,36))# out:120

#返回值2个以上时,使用元组:
fun=lambda x,y:(x//y,x%y)
print(fun(17,5))# out: (3, 2)

#返回值2个以上时,使用列表:
fun=lambda x,y:[x//y,x%y]
print(fun(17,5))# out:[3, 2]

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

#遍历列表中各元素:
print(list(filter(lambda x:x%3==0,foo)))
# out: [18, 9, 24, 12, 27]

print(list(map(lambda x:x%3==0,foo)))
# out: [False, True, True, False, False, True, False, True, True]
# 单行函数也可实现:
print(list(x for x in foo if x%3==0))
# out:[18, 9, 24, 12, 27]
# 单行函数也可实现:
print(list(x % 3 for x in foo))
# out:[2, 0, 0, 1, 2, 0, 2, 0, 0]

# 也可以"if...else..."来实现:
f=lambda x:"yes" if x%3==0 else "no"
print(list(map(f,foo)))

#列表作输入,返回用元组(使用统计函数):
fun=lambda a:(min(a),max(a),sum(a),sorted(a))
print(fun(foo))
# out:(2, 27, 139, [2, 8, 9, 12, 17, 18, 22, 24, 27])

#列表作输入,返回用列表(使用统计函数):
fun=lambda a:[min(a),max(a),sum(a),sorted(a)]
print(fun(foo))
# out:[2, 27, 139, [2, 8, 9, 12, 17, 18, 22, 24, 27]]
print("最大值:",fun(foo)[1],)
print("平均数:",fun(foo)[2]/(len(foo)))
print("前5位:",fun(foo)[3][0:5])
print("末5位:",fun(foo)[3][-1:-5:-1])
