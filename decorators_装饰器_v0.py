# 在这里写上你的代码 :-)
from functools import wraps #导入包装器

#在执行 beg 函数前,会先调用 say 函数,以判断 say_please 的值:
# beg 会先调用 say。如果返回的 say_please 为真，beg 会改变返回的字符串。

def beg(fun01):
    @wraps(fun01)
    # 打包:
    def wrapper(*args,**kwargs):
        msg,say_please=fun01(*args,**kwargs)
        if say_please:
            return "{0:s}{1:s}".format(msg,"Please! I am poor .")
        return msg
    return wrapper

@beg
def say(say_please=False):
    msg="Can you buy me a beer ？" #你能给我买杯啤酒吗?
    return msg,say_please


print(say())

#带参数使用:
print(say(say_please=True))
