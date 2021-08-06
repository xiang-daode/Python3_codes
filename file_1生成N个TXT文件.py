#生成5个文件:
for i in range(5):
    with open('f'+str(i)+'.txt',"w") as f:
        f.write('我不造病毒!')
