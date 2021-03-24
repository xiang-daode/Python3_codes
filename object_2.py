# 在这里写上你的代码 :-)
# 定义一个类A
class A:
    pass
a = A()
a.name = 'li'  # 能设置属性

# object没有定义__dict__，所以不能对object类实例对象尝试设置属性:
b = object()
b.name = 'wang' # 不能设置属性
