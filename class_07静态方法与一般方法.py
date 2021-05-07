# 导入标准库:
import math

# 自定义类:
class xMath():
    PI=3.14159265 #内置变量
    Num=99 #内置变量

   @staticmethod  #静态方法1,不用self
    def xor(i,j):
        return i^j

    @staticmethod  #静态方法2,不用self
    def myfun01(row,col,width):
        return width*row+col

    @classmethod  #类方法2用self ,调用内置的方法
    def myfun02(self,u,v,x,y):
        print(self.PI,self.Num)
        return self.xor(u+v,x+y)

    @classmethod  #类方法3用self ,修改了内置的变量
    def myfun03(self,k):
        self.PI*=k
        self.Num+=k
        return [self.PI,self.Num]

#调用自定义类中的各函数:
myCLS=xMath()
a=myCLS.xor(34,56)
b=myCLS.myfun01(4,6,100)
c=myCLS.myfun02(34,26,43,75)
print(a,b,c)
#传入数据并计算:
d=myCLS.myfun03(2)
print(d)
