# 在这里写上你的代码 :-)
import sys
#包括函数导入 myFunctions.py 模块
from myFunctions import myFun1 as myFun001
#__import__('myFunctions')        # 不包括函数导入 myFunctions.py 模块

v=myFun001(36,64)
print(v)
