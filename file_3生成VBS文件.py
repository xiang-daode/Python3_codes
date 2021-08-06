#生成100个文件:
for i in range(100):
    with open('f'+str(i)+'.vbs',"w") as f:
        f.write('\n MsgBox 2^24')
        f.write('\n MsgBox sin(7)')
        f.write('\n MsgBox now')
