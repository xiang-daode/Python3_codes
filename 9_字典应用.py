#======  字典应用  =======#

d = {"one": 1, "two": 2, "three": 3, "four": 4}
# {'one': 1, 'two': 2, 'three': 3, 'four': 4}
list(d)
# ['one', 'two', 'three', 'four']
list(d.values())
# [1, 2, 3, 4]
d["one"] = 42
# {'one': 42, 'two': 2, 'three': 3, 'four': 4}
del d["two"]
d["two"] = None
# {'one': 42, 'three': 3, 'four': 4, 'two': None}


dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# iteration
n = 0
for val in values:
    n += val
print(n) # 504

# keys and values are iterated over in the same order (insertion order)
list(keys)
# ['eggs', 'sausage', 'bacon', 'spam']
list(values)
# [2, 1, 1, 500]

# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
list(keys)
# ['bacon', 'spam']

# set operations
keys & {'eggs', 'bacon', 'salad'} #交集
# {'bacon'}
keys ^ {'sausage', 'juice'} #并集
# {'juice', 'sausage', 'bacon', 'spam'}