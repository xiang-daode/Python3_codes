import re

pattern = re.compile(r'([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.findall('cat Hello World 77 Wide Web 33')
print(m)

pattern = re.compile(r'([0-9]+)', re.I)   # re.I 表示忽略大小写
m = pattern.findall('cat Hello World 77 Wide Web 33')
print(m)

pattern = re.compile(r'(w[a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.findall('cat Hello World 77 Wide Web 33')
print(m)


