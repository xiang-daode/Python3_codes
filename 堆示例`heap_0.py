'''
heapq 模块提供了基于常规列表来实现堆的函数。 最小值的条目总是保持在位置零。
这对于需要重复访问最小元素而不希望运行完整列表排序的应用来说非常有用:
'''

from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

#把数据加入堆中:
heapify(data)                      # rearrange the list into heap order

#逐一压入，
heappush(data, -3)                 # add a new entry
heappush(data, -2)                 # add a new entry
heappush(data, -5)                 # add a new entry

#逐一弹出,已经自动按从小到大的顺序排序:
a3=[heappop(data) for i in range(len(data))]  # fetch the three smallest entries
print(a3)

#再逐一弹出，结果全部是空:
a4=[heappop(data) for i in range(len(data))]  # fetch the three smallest entries
print(a4)
