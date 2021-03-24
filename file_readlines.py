# 在这里写上你的代码 :-)
with open("生成学生册.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        print(line.split('\t'))
