# txtFile_覆盖式生成文件:
f = "myTest.txt"

a =[11,22,33,44]
with open(f,"w") as file:   #"w"代表着每次运行都覆盖内容
    for m in a:
        file.write(str(m)+":"+str(m**0.5)+"\n")

