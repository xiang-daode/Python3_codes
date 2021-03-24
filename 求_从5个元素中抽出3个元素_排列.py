# 从5个元素中抽出3个元素_排列, p=5*4*3=60
a = ["A", "B", "C", "D", "E"]

rs = [] #排列的结果
n = 0
for i in a:
    for j in a:
        if j != i:
            for k in a:
                if k != i and k != j:
                    rs.append([i, j, k])
                    n = n + 1
for m in rs:
    print(''.join(m),m)
print(n)
