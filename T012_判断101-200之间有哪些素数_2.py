# 在这里写上你的代码 :-)
'''
题目012：判断101-200之间有多少个素数，并输出所有素数。
'''
def tm012():
   num=0;
   for i in range(101,201):
       if zs(i):
          num=num+1
   print("\nCount=",num)

# 判断n是否质数:
def zs(x):
    f=0
    for i in range(2,x):
        if x%i==0:
            f=1
            break;
    if f==1:
       return False
       # print("不是质数")
    if f==0:
        print(x,end=',') #"是质数"
        return True


print(tm012())
