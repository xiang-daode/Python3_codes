# 在这里写上你的代码 :-)
'''
题目062：查找字符串。
'''

s = 'abc,CBA'
print(s.find('c'))#2

s = 'ab,cd,ef'
print(s.find(',')) #2


#=======  以下使用正则表达式  ========
import re

s = 'a88,b99,c77,d33,e22'
print(re.findall(r'(\D+)',s))  #不要数字['a', ',b', ',c', ',d', ',e']

s = 'a88,b99,c77,d33,e22'
print(re.findall(r'(\d+)',s)) #只要数字['88', '99', '77', '33', '22']


s = 'My god,学习编程是神人,hi! 神人,牛人皆来了'
print(re.findall(r'([\u4e00-\u9fa5]+)',s))#只要中文 ['学习编程是神人', '神人', '牛人皆来了']
print(re.findall(r'([a-zA-Z]+)',s))#只要英文['My', 'god', 'hi']
