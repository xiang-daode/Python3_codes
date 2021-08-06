################    读取文件-3:逐行读取两字段:(姓名,英语)的常用统计,列表应用    ####################
#姓名0  班级1  语文2  数学3  英语4  科学5  社会6  总分7
with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    nm=[];en=[]
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组
        print(s2[0],s2[4])
        if i>0: #跳过中文表头
            nm.append(s2[0])
            en.append(int(s2[4])) #转为整数,再添加到列表中
        i=i+1
fr.close()
print("人数:{0},总和:{1},最高:{2},最低:{3},平均:{4:0.2f}"
.format( len(en),sum(en),max(en),min(en),sum(en)/len(en)))
#作业:统计"语文","数学","总分"之各项数据,再生成HTML表格,以便上报.
