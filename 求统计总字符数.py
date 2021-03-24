'''
统计0,1,2,3,...,num这些数里,
共出现了多少个字符?
如,'321'作3个字符计
2894
'''

num=1000
cnt=0
for i in range(num+1):
    s=str(i)
    cnt=cnt+len(s)
    #print(i,cnt)
print("Count of char : ",cnt)
