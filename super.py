# 在这里写上你的代码 :-)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class A(object):   # Python2.x 记得继承 object
    def add(self, x):
         y = x+1
         print(y)
class B(A):
    def add(self, x):
        super(B, self).add(x)
b = B()
b.add(2)  # 3
