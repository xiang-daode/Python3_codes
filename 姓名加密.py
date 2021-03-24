# 姓名加密
a=0x9879
b=0x9053
c=0x5fb7
print(chr(a),chr(b),chr(c))#原姓名
print(chr(a+31),chr(b+31),chr(c+31))#加密姓名-1
print(chr(a-7),chr(b-7),chr(c-7))#加密姓名-2
print(chr(a^1234),chr(b^1234),chr(c^1234))#异或算法---加密姓名-3
