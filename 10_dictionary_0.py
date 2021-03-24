#!/usr/bin/python
# -*- coding: cp936 -*-

#声明字典:
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

#对词典内各个值的数字求和:
n = 0
for val in values:
     n += val
print(n)
# show: 504

# keys and values are iterated over in the same order (insertion order)
print(list(keys))#列出字典中所有的键，
# show: ['eggs', 'sausage', 'bacon', 'spam']
print(list(values))#列出字典中所有的值，
# show: [2, 1, 1, 500]

# view objects are dynamic and reflect dict changes
#从字典中删除两个元素:
del dishes['eggs']
del dishes['sausage']
print(list(keys))
# show: ['bacon', 'spam']

# set operations

#求两个集合的交集:
v=keys & {'eggs', 'bacon', 'salad'}
print(v)
# show: {'bacon'}

#对两个集合求异或:
w=keys ^ {'sausage', 'juice'}
print(w)
# show: {'juice', 'sausage', 'bacon', 'spam'}



