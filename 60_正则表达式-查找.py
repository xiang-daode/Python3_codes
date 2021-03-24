import re

#查找‘f’开头的单词:
s=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(s) #['foot', 'fell', 'fastest']

#查找包含‘o’的单词:
s=re.findall(r'\b[a-z]*[o][a-z]*', 'which foot or hand fell fastest')
print(s) #['foot', 'or']

#查找‘t’结尾的单词:
s=re.findall(r'\b[a-z]*[t]', 'which foot or hand fell fastest')
print(s) #['foot', 'fastest']

text = "JGood is a  handsome boy,he is handsome and cool,clever,and so on ...."
print (re.findall(r'\w+',text)) #结果：['JGood', 'is', 'a', 'handsome', 'boy', 'he', 'is', 'handsome', 'and', 'cool', 'clever', 'and', 'so', 'on']

text = "JGood is a 7788 handsome boy,he 4455 is handsome and cool,clever,and so on ...."
print (re.findall(r'\d+',text)) #结果：, ['7788', '4455']

