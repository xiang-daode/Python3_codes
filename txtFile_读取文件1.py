# 在这里写上你的代码 :-)
filename = 'MyTest.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径


with open(filename, 'r') as file_to_read:
  while True:
     lines = file_to_read.readline() # 整行读取数据
     if(len(lines)<5):
        break;
     b=lines.split('\t')
     print(b)



