#题目:在1--1000之内,找出所有的质数
#         其他的代码700多个,在我的仓库:
# url_1:  https://github.com/xiang-daode/Python3_codes
# url_2:  https://gitee.com/xiang-daode/Python3_codes

#!/usr/bin/python
# -*- coding: cp936 -*-
from math import sqrt

#单行写法:
#print(" ".join("%s"% x for x in range(2,1000)if not [y for y in range(2,1+int(sqrt(x)))if not x%y]))


#解释1:是合数的,输出各因数:
for x in range(2,100):
    print(x,":")
    for y in range(2,x-1): #range(2,1+int(sqrt(x)))
         if x%y==0:  # not x%y: 如同: x%y==0 ,因为非0是True, 0即False
             print(y,end=',')
    print('<<<===============')

#解释2:先不管拼接为字符串之事,生成个列表a1,  print(a1) #输出是列表:
a1=[x for x in range(2,1000)if not [y for y in range(2,1+int(sqrt(x)))if not x%y]]
#     {  2,3,4,  ...,   999}若  非  {            合数(非质数)                     }


#解释3:将所有数字元素转为字符串,插入空格拼接成长字符串,输出是字符串:
print(" ".join("%s"%  m for m in  a1))


'''解释4:传统的多行写法:
for x in range(2,1000):
    f=1
    for y in range(2,1+int(sqrt(x))):
        if  x%y ==0:
            f=0
    if f==1:
        print(x,end=',')
'''





