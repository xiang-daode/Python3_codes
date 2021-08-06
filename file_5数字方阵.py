#生成1个文件:

with open('f5.txt',"w") as f:
    for i in range(10000):
        f.write(str(i % 10)+'_')
        if(i%10==0):
            f.write('\n')
