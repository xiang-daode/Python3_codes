for m in range(1,360):
    if m % 5==0 and m % 7==0:
         print(m,"(5&&7)")    
    elif m % 17==0 or m % 19==0:
         print(m,"17||19")
