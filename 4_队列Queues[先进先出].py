# 队列Queues[先进先出]:
from collections import deque

queue = deque(["son1", "son2", "son3"])
print(queue)
#追加到最后边:
queue.append("son4")
print(queue)
queue.append("son5")
print(queue)
#从左边弹出:
q=queue.popleft()
print(q,queue)
q=queue.popleft()
print(q,queue)

