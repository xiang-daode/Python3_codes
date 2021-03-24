# 在这里写上你的代码 :-)
#!/usr/bin/python
# -*- coding: cp936 -*-

s="项道德"
print (s.encode("GBK"))


s="项,道,德"
print (s.encode("UTF-8"))

s="项,道,德"
a=s.split(',')
print (hex(ord(a[0])),hex(ord(a[1])),hex(ord(a[2])))

s0="项道德"
s1=s0.encode("GBK")

print(type(s1),s1.decode(encoding="gbk"))
