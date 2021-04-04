# 用5个元素中的3个元素组成字符串_排列, p=5*5*5=125
a = ["A", "B", "C", "D", "E"]

rs = []  # 排列的结果
n = 0
for i in a:
    for j in a:
        for k in a:
            rs.append([i, j, k])
            n = n + 1
for m in rs:
    print("".join(m), m)
print(n)
