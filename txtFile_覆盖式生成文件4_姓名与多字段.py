# txtFile_覆盖式生成文件:
import random
f = "myTest.txt"

a =range(200)
with open(f,"w") as file:
    file.write("序号:  \t姓名  \t年龄  \t存款")
    for m in a:
        d1=int(20902*(random.random()))
        d2=int(20902*(random.random()))
        user="项"+chr(0x4e00+d1)+chr(0x4e00+d2)
        file.write("\n"+str(m)+":  \t"+user)
        file.write("  \t"+str(d1 % 120))
        file.write("  \t"+str(d2 % 1500))
print(f+"---文件已经生成!")
