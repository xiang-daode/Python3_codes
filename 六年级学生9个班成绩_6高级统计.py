################    读取文件-6:逐行读取两字段:(姓名,英语)的高级统计,列表应用    ####################

with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    nm=[];MyList=[]
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        print(s2[0],s2[4])
        if i>0: #跳过中文表头
            nm.append(s2[0])
            MyList.append(int(s2[4])) #转为整数,再添加到列表中
        i=i+1
fr.close()

import numpy as np #依赖numpy库计算List

#计数与求和:
a_sum = np.sum(MyList)
print("个数=%d" % len(MyList),",和为：%0.2f" % a_sum)
#求均值:
a_mean = np.mean(MyList)
print("平均值为：%0.2f" % a_mean)
#求方差:
a_var = np.var(MyList)
print("方差为：%0.2f" % a_var)
#求标准差:
a_std = np.std(MyList,ddof=1)
print("标准差为:%0.6f" % a_std)

