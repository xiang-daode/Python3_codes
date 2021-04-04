# 在这里写上你的代码 :-)

#题目055_正则全文搜索

import re

phone = '''2004-959-559 # 这是一个电话号码@
2021-334-778 # 这又是一个电话号码@
'''
# 移除非数字的内容
#num = re.sub(r'\D', "", phone)
#print ("电话号码 : ", num)

# 删除注释
num = re.sub(r'#.*@', "", phone)
#print ("#[这里内容已经替换]@", num)

# 删除中文字:
num = re.sub(r'[\u4e00-\u9fa5]*', "", phone)
print ("", num)


line = "Cats are smarter[更聪明些] than dogs(有些狗要例外的,如机器狗)"

matchObj = re.match( r'(Cats).*([\u4e00-\u9fa5]+).*(dogs)', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
   print ("match --> matchObj.group(0) : ", matchObj.group(0))
   print ("match --> matchObj.group(1) : ", matchObj.group(1))
   print ("match --> matchObj.group(2) : ", matchObj.group(2))
   print ("match --> matchObj.group(3) : ", matchObj.group(3))
else:
   print ("No match!!")

#全文搜索,找出中文字,返回是列表[]:
s=re.findall(r'[\u4e00-\u9fa5]+',line)
print(s)



