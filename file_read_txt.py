# 文本方式,读取GBK编码的文件:
f = open('test_GBK.txt','rt')
txt=f.read()
print(txt)


# 文本方式,读取UTF-8编码的文件:
f = open('test_UTF8.txt','rt',-1,"UTF-8")
txt=f.read()
print(txt)

#  二进制方式,读取UTF-8编码的文件:
f = open('test_UTF8.txt','br')
txt=f.read()
print(txt)
