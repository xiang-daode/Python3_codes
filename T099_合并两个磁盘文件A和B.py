# 在这里写上你的代码 :-)
'''
题目099：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
#合并两文件:
with open('a.txt','r') as f:a=f.read()
with open('b.txt','r') as f:b=f.read()
s = ''.join(sorted(list(a+b))) # 字符串排序(假设全为大写字母): 转为list,字符排序后再拼接回字符串
with open('T099_ab.txt','w') as f:f.write(s)
