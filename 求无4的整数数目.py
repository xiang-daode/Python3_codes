'''
统计0,1,2,3,...,num这些数里,
不出现4的数字有多少个?
730

'''

num=1000
cnt=0
for i in range(num+1):
    s=str(i)
    if not ('4' in s):
      cnt=cnt+1
      #print(i,cnt)
print("Count of char except '4' : ",cnt)
