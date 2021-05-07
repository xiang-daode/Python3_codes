# 在1--10001中,同时是3,7的倍数的数有哪些?
for i in range(1,10001):
    if i%3==0 and i%7==0:
        print(i,end=',')



