#生成1个文件:

with open('f5.txt',"w") as f:
    for i in range(10000):
        f.write('\n'+str(i)+'^2:'+ str(i*i))
