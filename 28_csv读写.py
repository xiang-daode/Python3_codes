import csv

# 读取csv文件
with open('test.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for line in reader:
        print(line)

# 写
with  open('test.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(["index", "a_name", "b_name"])
    writer.writerows([[1, 2, 3], [0, 1, 2], [4, 5, 6]])

