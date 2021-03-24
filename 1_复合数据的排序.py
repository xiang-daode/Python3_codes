a=[1,9,2,8,3,7,4,6,5,0]
a.sort()
print(a,'<<----sorted array',len(a),max(a),min(a),a.count(3),sum(a)/len(a),"<<==The end")

#字符串分割成数组,并以小写字母为关键字进行排序:
s="This is a test string from Andrew"
sa=sorted(s.split(), key=str.lower)
print(sa)

#字符串分割成数组,并以小写字母为关键字进行排序:
s="This,is,a,test,string,from,Andrew"
sa=sorted(s.split(','), key=str.lower,reverse=True)
print(sa)

#复合对象的内容的排序,可以拿下标作关键字排序:
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
a3=sorted(student_tuples, key=lambda student: student[2])
# sort by age:
print(a3)
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


