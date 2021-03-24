import re

pattern = re.compile(r"\d+")
lst = pattern.findall("abc1def2rst3xyz")  # findall
print(lst)

# 输出结果：
# ['1', '2', '3']
