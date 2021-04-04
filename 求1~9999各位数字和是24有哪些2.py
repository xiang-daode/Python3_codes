# 1~9999各位数字和是24有哪些

def myFun():
    count=0 #符合条件的计数
    for i in range(1, 9999):
        num = len(str(i))
        lst=list(str(i)) #将每个数字拆成单一字符,组成列表
        sum=0
        for j in range(num):
           sum+=int(lst[j])
        #求和之后判断:
        if sum==24:
            print(lst)
            count+=1

    print('count=',count)
myFun()
