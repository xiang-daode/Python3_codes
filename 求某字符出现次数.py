'''
统计0,1,2,3,...,num这些数里,'8'出现过多少次?
如'188,883,808'各数中,都算出现2次

'''

num=1000
cnt=0
for i in range(num+1):
    s=str(i)
    if '8' in s:        
        cnt=cnt+s.count('8')
        #print(i,s.count('8'),cnt)
print("Count of char '8' : ",cnt)
