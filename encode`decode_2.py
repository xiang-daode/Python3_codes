# 在这里写上你的代码 :-)
s1="项道德".encode("GBK")
print(s1)#编码结果: b'\xcf\xee\xb5\xc0\xb5\xc2'

a1=bytes(s1)
print(len(a1),type(a1)) #输出: 6 <class 'bytes'>

s2=s1.decode("GBK")
print(s2)#解码结果: 项道德

#加密方法:用列表mylist装载各元素(值范围:0...255),然后装入bytes(mylist)
lt=[]
for i in range(len(a1)):
    #lt.append(a1[i]+7)
    #print(a1[i]+7,end=',')
    lt.append((a1[i]*63) % 256)
    print((a1[i]*63) % 256,end=',')
s3=bytes(lt).decode("GBK")
print(s3)#駫婡嬀

