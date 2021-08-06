#list下关于字符串的选择性搜索
a=["cat","fox","pig","dog","bee","ant","cow"]
for m in a: #1,哪些动物包含字符'o'的?
    if 'o' in m:
        print(m,end=';')
print()
for m in a:  #2,哪些动物以字符'c'作开头的?
    if m[0]=='c':
        print(m,end=';')
print()
for m in a: #3,哪些动物以字符'g'作结尾的?
    if m[-1]=='g':
        print(m,end=';')
print()
#4,按字母排序各动物
b=sorted(a)   # 倒序:b=a[::-1] ,   排序用函数: b=sorted(a)
print(b)

