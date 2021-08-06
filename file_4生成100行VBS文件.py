#生成100个文件:
for i in range(100):
    with open('f'+str(i)+'.vbs',"w") as f:
        for i in range(100):
            f.write('\n MsgBox now')
