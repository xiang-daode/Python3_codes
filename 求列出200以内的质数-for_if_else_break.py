for n in range(2, 200):
    for x in range(2, n-1):
        if n % x == 0:
            print(n, ' = ', x, '*', n//x,end=',')
            break
    else:
        print('\n',n, '========>>> prime number')
