
sum(i*i for i in range(10))                 # sum of squares


xvec = [10, 20, 30]
yvec = [7, 5, 3]
s1=sum(x*y for x,y in zip(xvec, yvec))         # dot product
print(s1)

from math import pi, sin
s2=sine_table = {x: sin(x*pi/180) for x in range(0, 3)}
print(s2)


#unique_words = set(word  for line in page  for word in line.split())


#valedictorian = max((student.gpa, student.name) for student in graduates)



data = '2*22=44'
s3=list(data[i] for i in range(len(data)-1, -1, -1))
print(s3)
