# 从5个元素中抽出3个元素_组合方案, C=(5*4*3)/(1*2*3)=10
a = ["A", "B", "C", "D", "E"]

rs = [] #组合的结果
n = 0
for i in range(5):
    for j in range(i+1,5):
            for k in range(j+1,5):
                    rs.append((a[i], a[j], a[k]))
                    n = n + 1
for m in rs:
    print(''.join(m),m)
print(n)
