# set_集合与运算
#初始化与搜索:
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) #自动删除重复后为:{'orange', 'banana', 'pear', 'apple'}
print('orange' in basket) #找到了:True
print('crabgrass' in basket) #找不到的:False

# 在两个词汇中,独立字母的操作范例:
# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
# a中独一无二的字母:
print(a,b) #a is :{'a', 'r', 'b', 'c', 'd'} {'l', 'z', 'c', 'm', 'a'}

z=a - b  #"差" 在a中,但不在b中
print(z) #z is :{'r', 'd', 'b'}

z=a | b  #"或,合并,并" 在a中,或在b中
print(z) #z is :{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

z=a & b #"与", 同时在a,b中
print(z) #z is :{'a', 'c'}

z=a ^ b #异或, letters in a or b but not both(在a中或在b中,但是不同时在(a,b)中)
print(z) #z is :{'r', 'd', 'b', 'm', 'z', 'l'}

#搜索在A中,但是不在B中的元素:
z = {x for x in 'abracadabra' if x not in 'abc'}
print(z) #z is :{'r', 'd'}
print(set('abracadabra')-set('abc')) #同等效果#{'r', 'd'}



