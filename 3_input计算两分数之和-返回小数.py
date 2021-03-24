
#计算两分数之和,返回小数
s= input("Please enter 4 num ,as 1,2,3,4:  ")
sa=s.split(',')
print(sa)

a1=float(sa[0])
a2=float(sa[1])
a3=float(sa[2])
a4=float(sa[3])  

if a2 !=0 and a4 !=0:
       print ("a1/a2+a3/a4= ",a1/a2+a3/a4)
if a2 ==0 or a4 ==0:
       print('a1/a2+a3/a4 <<<--- must:  a2 != 0 ,a4 != 0  ')

