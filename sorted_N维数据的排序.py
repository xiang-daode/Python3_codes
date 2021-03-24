#!/usr/bin/python


list3D=[('2','3','9'),('1','2','8'),('5','6','5'),('2','5','3'),('2','4','7')]
print("默认方式进行排序:\n",sorted(list3D))

print("按第3关键字和第2关键字进行排序:")
print(sorted(list3D, key = lambda x:(x[2],x[1])))

