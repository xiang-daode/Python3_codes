#列出100以内5的倍数:
a=0
while a <= 100:
    if a % 5==0:
        print(a,end='|')
    a=a+1

#计算100!=?
b=1
a=1
while a <= 100:
    b=b*a
    a=a+1
print('\n 100!=',b)
   
