# 在这里写上你的代码 :-)
'''
题目043：类中建立具有记忆功能的静态变量(static)。
'''
class staticDemo:
    static001=100
    def tm043(self,i):
        self.static001+=i
        return self.static001


A=staticDemo()
print(A.tm043(1))
print(A.tm043(2))
print(A.tm043(3))
print(A.tm043(4))
