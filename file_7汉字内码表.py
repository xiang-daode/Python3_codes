#生成1个文件:

with open('f5.txt',"w") as f:
    for i in range(1000):
        cd=0x4e00+i;
        s2=chr(cd)
        f.write('\n'+hex(cd)+':'+s2)
