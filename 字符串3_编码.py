# 在这里写上你的代码 :-)
s='一' #单一的汉字
print(ascii(s)) #返回Unicode编码,16进制
print(ord(s))   #返回Unicode编码,10进制
print(hex(ord(s)))  #返回Unicode编码,16进制
print(s.encode("GBK")) #返回GBK编码,16进制
print(s.encode("UTF-8")) #返回UTF-8编码,16进制
print("==========查查你爸的姓名==============")

