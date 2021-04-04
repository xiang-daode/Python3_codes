# 1~9999(万内)字符'0'和'8'各出现了几次?

n0 = 0 # 统计字符'0'出现了几次
n8 = 0 # 统计字符'8'各出现了几次

nu0 = 0 # 统计无字符'0'出现了几次
nu8 = 0 # 统计无字符'8'各出现了几次

for i in range(1, 10000):
    num = len(str(i))
    lst=list(str(i))
    if '0' in lst:
       n0+=1
    if '8' in lst:
       n8+=1
    if '0' not in lst:
       nu0+=1
    if '8' not  in lst:
       nu8+=1
print(n0,n8)
print(nu0,nu8)
''' 输出:
2619 3439
7380 6560
'''
