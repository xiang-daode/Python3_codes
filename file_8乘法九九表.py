#生成1个文件:

with open('f5.txt',"w") as f:
    for i in range(1,10):
        for j in range(1,i+1):
            f.write(str(j)+"x"+str(i)+"="+str(i*j)+'\t')
        f.write('\n')