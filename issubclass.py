#!/usr/bin/python
# -*- coding: UTF-8 -*-

class A:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# 重新定义初始化函数时,原参数作废了:
class B(A):
  def __init__(self, name2, age2):
    self.name2 = name2
    self.age2 = age2

# 重新定义初始化函数时,原参数作废了:
class C(B):
  def __init__(self, name3, age3):
    self.name3 = name3
    self.age3 = age3
  def myShow(self):
    print(self.name3, "was", self.age3,"years old !")

# 完全地继承时,用上原来的参数:
class D(A):
    pass

print(issubclass(B,A))    # 返回 True
print(issubclass(A,B))    # 返回 False
print(issubclass(C,B))  #  返回 True
print(issubclass(C,A))  #  返回 True
print(issubclass(D,A))  #  返回 True
print(globals())
x=A("dd",99)
print(x.name,x.age)
y=B("xdd",88)
print(y.name2,y.age2)
y=C("xiang.dd",111)
print(y.name3,y.age3)
print(y.myShow())
x=D("dd88",8899)# 完全地继承时,用上原来的参数
print(x.name,x.age)

