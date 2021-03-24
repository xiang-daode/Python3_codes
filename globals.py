# 在这里写上你的代码 :-)
a=777
print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。
b=11,22,33
c={"A":88,"B":44}
print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。
print(globals()['a'],globals()['b'],globals()['c']) # 读取某变量值
print(globals()['__file__']) # 返回当前执行文件,自己的文件名与路径
