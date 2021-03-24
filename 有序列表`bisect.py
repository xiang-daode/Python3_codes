import bisect

'''
有序列表---对插入的各种元素,自动按照第一关键字进行自动排序，

'''
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'C#'))
bisect.insort(scores, (370, 'H5'))
bisect.insort(scores, (330, 'java'))
bisect.insort(scores, (30, 'fox'))
bisect.insort(scores, (37, 'pig'))
bisect.insort(scores, (33, 'cat'))

print(scores)
