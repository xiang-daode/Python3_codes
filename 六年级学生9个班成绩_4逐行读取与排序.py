################    读取文件-4:逐行读取两字段:(姓名,英语)的常用统计,字典应用    ####################
# list tuple set dict stack queue
with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    dt={} #定义字典,名称,变量名: dt  dt['fox']=12,dt={"fox"=12}
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        #print(s2[0],s2[4])
        if i>0: #跳过中文表头
            dt[s2[0]]=int(s2[4]) #向字典中添加"键-值"对
        i=i+1
fr.close()
print("人数:{0}".format(len(dt)))

#按英语成绩排序(从小到大),带姓名输出, d[0]:姓名, d[1]:值
dt2=sorted(dt.items(), key=lambda d: d[1], reverse=False)
#print(dt2);print()

#按英语成绩排序(从大到小),带姓名输出:
dt3=sorted(dt.items(), key=lambda d: d[1], reverse=True)
#print(dt3);print()
for m in dt3:
    #print(m)
    #print(m[0],m[1])
    print(m[0]+": "+str(m[1])+"分")


#按姓氏内码(从大到小),带姓名输出:
dt4=sorted(dt.items(), key=lambda d: d[0])
#print(dt4);print()

