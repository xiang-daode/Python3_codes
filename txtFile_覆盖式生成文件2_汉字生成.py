# txtFile_覆盖式生成文件:
f = "myTest.txt"

a =list(range(200))
with open(f,"w") as file:   #"w"代表着每次运行都覆盖内容
    for m in a:
        file.write(str(m)+":"+chr(0x4e00+m)+"\n")


