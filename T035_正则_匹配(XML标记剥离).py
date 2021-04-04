# 在这里写上你的代码 :-)
'''
题目035：正则_匹配。
'''
import re


line = "<h4>pigs</h4> are bigger then <h5>cats</h5>"

matchObj = re.match(r'<h4>(.*)</h4> .* <h5>(.*)</h5>', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match !")

''' 输出结果:
matchObj.group() :  <h4>pigs</h4> are bigger then <h5>cats</h5>
matchObj.group(1) :  pigs
matchObj.group(2) :  cats
'''
