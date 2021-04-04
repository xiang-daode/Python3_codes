# 1~9999包含'18'的统计
# import string

# find()函数用法:
# 在s中找不到'18'时: s.find('18')=-1,找到的返回下标:0,1,2,3,...
# print('1800'.find('18'))#找到的,返回下标0
# print('7718'.find('18'))#找到的,返回下标2

c = 0
for i in range(1, 9999 + 1):
    ln = len(str(i))
    if ln >= 2 and (str(i).find("18") != -1):
        print(i)
        c += 1
print("Count=", c)
