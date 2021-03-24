n,m=36,48  # n<=m
i=m-n
while i>=2:
    if (n % i==0) and (m % i==0):
       print(i,end='---GCD')
       break
    i=i-1   
print()
j=n
while j<=m*n : 
    if (j%n==0) and (j%m==0):
      print(j,end='---LCM') 
      break
    j=j+1  
print()      
print("="*50)        
