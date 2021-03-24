#!/usr/bin/python
# -*- coding: cp936 -*-

#�����ֵ�:
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

#�Դʵ��ڸ���ֵ���������:
n = 0
for val in values:
     n += val
print(n)
# show: 504

# keys and values are iterated over in the same order (insertion order)
print(list(keys))#�г��ֵ������еļ���
# show: ['eggs', 'sausage', 'bacon', 'spam']
print(list(values))#�г��ֵ������е�ֵ��
# show: [2, 1, 1, 500]

# view objects are dynamic and reflect dict changes
#���ֵ���ɾ������Ԫ��:
del dishes['eggs']
del dishes['sausage']
print(list(keys))
# show: ['bacon', 'spam']

# set operations

#���������ϵĽ���:
v=keys & {'eggs', 'bacon', 'salad'}
print(v)
# show: {'bacon'}

#���������������:
w=keys ^ {'sausage', 'juice'}
print(w)
# show: {'juice', 'sausage', 'bacon', 'spam'}



