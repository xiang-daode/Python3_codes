# deque_队列(先进先出),要实现队列，请使用collections.deque，它的设计目的是从两端快速添加和弹出
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
z= queue.popleft()  # 'Eric'
z= queue.popleft()   #'John'
print(queue )   #deque(['Michael', 'Terry', 'Graham'])
