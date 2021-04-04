# 在这里写上你的代码 :-)
'''
题目041：静态变量具有记忆。
'''


# StaticA,StaticB,StaticC作为类的一个属性，相当于静态变量,在多次执行后,具有记忆特征:
class Static:
    StaticA = .25
    StaticB = .50
    StaticC = .75
    def varfunc(self,x):
        self.StaticA += .0025
        self.StaticB += .0050
        self.StaticC += .0075
        return(10*x,": ",self.StaticA*x,self.StaticB*x,self.StaticC*x)

#创建类之实例:
a = Static()
#N次执行类中的函数:
for i in range(11):
    print(a.varfunc(i/10))

