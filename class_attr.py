# 在这里写上你的代码 :-)
class Person:
  name = "fox"
  age = 6
  color = "red"
  qq = "123456789"
# 将年龄修改为9:
setattr(Person, 'age', 9)
x=hasattr(Person, 'age') # 判断有无'age'属性
y=getattr(Person, 'age') # 读取属性'age'值
print(x,y,hasattr(Person, 'qq')) # 输出三者内容(x,y,hasattr(Person, 'qq'))
delattr(Person, 'qq')  # 删除'qq'属性
print(hasattr(Person, 'qq')) # 判断有无属性'qq'


