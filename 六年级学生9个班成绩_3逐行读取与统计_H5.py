################    读取文件-3:逐行读取两字段:(姓名,英语)的常用统计,列表应用    ####################
#姓名0  班级1  语文2  数学3  英语4  科学5  社会6  总分7
with open('六年级学生9个班成绩.txt',"r") as fr:
    i=0
    yw=[];sx=[];zf=[]
    while True:
        s0=fr.readline()
        if len(s0)<2:
            break;
        s1=s0.replace('\n','') #去掉换行符
        s2=s1.split('\t') #按制表符拆分成元组

        if i>0: #跳过中文表头
            yw.append(int(s2[2])) #转为整数,再添加到列表中
            sx.append(int(s2[3])) #转为整数,再添加到列表中
            zf.append(int(s2[7])) #转为整数,再添加到列表中
        i=i+1
fr.close()

L2=(len(yw),sum(yw),max(yw),min(yw),sum(yw)/len(yw)) #语文
L3=(len(sx),sum(sx),max(sx),min(sx),sum(sx)/len(sx)) #数学
L7=(len(zf),sum(zf),max(zf),min(zf),sum(zf)/len(zf)) #总分

T='''<center><h1>六年级期末成绩统计表</h1><hr><table border=1 bgcolor="#FED" width=60%>
  <tr>  <td>制表人:项道德</td>  <td>人数</td>   <td>总数</td>    <td>最高</td>    <td>最低</td>    <td>均值</td> </tr>
  <tr>  <td>语文</td>  <td>@00</td>    <td>@01</td>    <td>@02</td>    <td>@03</td>    <td>@04</td> </tr>
  <tr>  <td>数学</td>  <td>@10</td>    <td>@11</td>    <td>@12</td>    <td>@13</td>    <td>@14</td> </tr>
  <tr>  <td>总分</td>  <td>@20</td>    <td>@21</td>    <td>@22</td>    <td>@23</td>    <td>@24</td> </tr>
</table>'''
#语文的五次替换:
T=T.replace("@00",str(L2[0]))
T=T.replace("@01",str(L2[1]))
T=T.replace("@02",str(L2[2]))
T=T.replace("@03",str(L2[3]))
T=T.replace("@04",str(L2[4]))

#数学的五次替换:
T=T.replace("@10",str(L3[0]))
T=T.replace("@11",str(L3[1]))
T=T.replace("@12",str(L3[2]))
T=T.replace("@13",str(L3[3]))
T=T.replace("@14",str(L3[4]))

#总分的五次替换:
T=T.replace("@20",str(L7[0]))
T=T.replace("@21",str(L7[1]))
T=T.replace("@22",str(L7[2]))
T=T.replace("@23",str(L7[3]))
T=T.replace("@24",str(L7[4]))

#生成有表格的HTML文件:
with open("CLS_6.html","w") as fw:
    fw.write(T)
fw.close()

print("CLS_6.html ---文件已经生成,请查看.")
