#双向队列:
from collections import deque

d = deque(["task1", "task2", "task3"])
d.append("task4")
d.append("task0")
d.append("taskA")

print("Handling", d.popleft())
print([x for x in d])
print([x for x in d.popleft()])
print([x for x in d.pop()])




