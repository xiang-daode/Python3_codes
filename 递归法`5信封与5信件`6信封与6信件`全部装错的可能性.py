# 递归法,5信封与5信件,6信封与6信件:全部装错的可能性

def fun(n):
    if n==1 :
        return 0
    if n==2 :
        return 1
    if n>2:
        return (n-1)*(fun(n-1)+fun(n-2))

print("n=5: ",fun(5))
print("n=6: ",fun(6))




