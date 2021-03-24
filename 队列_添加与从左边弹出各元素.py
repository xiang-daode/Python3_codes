from collections import deque


d = deque([])
for i in range(17):
    d.append(str(i))
    print(str(i), end=';')
print('\n', d)

#从左边弹出各元素，适用于实现队列和广度优先树搜索：
for i in range(17):
    print("#", d.popleft(), end=';')

