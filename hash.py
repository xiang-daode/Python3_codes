# 在这里写上你的代码 :-)

# 返回对象的哈希值,16位的16进制数:
a=hash('test')            # 字符串

b= hash(1)                 # 数字

c= hash(str([1,2,3]))      # 集合

d= hash(str(sorted({'1':1}))) # 字典

print(a,b,c,d)
print(hex(a),hex(b),hex(c),hex(d))
