# 在这里写上你的代码 :-)

# 内置的@property装饰器就是负责把一个方法变成属性调用的:
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score=88
print("88 ---OK")
# s.score='33' ---这样会触发:'score must be an integer!'
# s.score=9999  ---这样会触发:'score must between 0 ~ 100!'
