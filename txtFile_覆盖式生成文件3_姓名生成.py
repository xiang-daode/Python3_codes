# txtFile_覆盖式生成文件:
import random
f = "myTest.txt"

a =range(200)
with open(f,"w") as file:   #"w"代表着每次运行都覆盖内容
    for m in a:
        rnd1=int(20902*(random.random()))
        rnd2=int(20902*(random.random()))
        file.write(str(m)+":\t 项"+chr(0x4e00+rnd1)+chr(0x4e00+rnd2)+"\n")


