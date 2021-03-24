# 在这里写上你的代码 :-)

# 创建新文件(原有文件被覆盖),并写入内容:
fo = open("foo.txt", "w+")
fo.write('===================')
fo.write('\nhttp://www.runoob.com/')
fo.write('\n一二三,项道德')
fo.write('\n********************')
fo.flush() #涌流


fo.seek(0) # 指针移动到文件开头
txt=fo.read()# 读取全文
print (txt)
# 读取指定的行:
ls=txt.split('\n')
print (len(ls)) # 总行数=4,可用序号:0,1,2,3
print (ls[3])

fo.close()
