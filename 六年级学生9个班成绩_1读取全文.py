################    读取文件-1:直接扫描文件中的全文并输出    ####################

with open('六年级学生9个班成绩.txt',"r") as fr:
    txt=fr.read()
    print(txt)
fr.close()

