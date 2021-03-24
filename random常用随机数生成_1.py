import random


w=random.choice(['apple', 'pear', 'banana'])
print(w)  #as :'apple'

s=random.sample(range(100), 10)   # sampling without replacement
print(s)  #as :[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]

v=random.random()    # random float
print(v)  #as :0.17970987693706186

h=random.randrange(6)    # random integer chosen from range(6)
print(h)  #as :4

