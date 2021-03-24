#定义类,表示学生的姓名,等级,年龄:
class Student:
     def __init__(self, name, grade, age):
         self.name = name
         self.grade = grade
         self.age = age
     def __repr__(self):
         return repr((self.name, self.grade, self.age))


#有三个学生的数据作数组:
student_objects = [
     Student('john', 'A', 15),
     Student('jane', 'B', 12),
     Student('dave', 'B', 10),
 ]

#以学生年龄为关键字排序:
a1=sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(a1)




