
a=[1,7,2,9,3,6,4,5,8]
n,s=0,0
for x in a:
   n=n+1
   s=s+x
print("sum=",s,",avg=",s/n)

qt=0
avg=s/n
for x in a:
	  qt=qt+(x-avg)**2
print("std=",pow(qt/n,0.5))	  	

