for num in range(12, 60):
    if num==50:
        break
    if num % 10 == 0:
        print("Found an 10X number:", num)
        continue
    if num % 2 == 0:
        print("Found an even number:", num)
        continue    
    print(" ", num)
