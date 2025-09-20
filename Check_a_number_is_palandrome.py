def palandrome(n):
    n1=int(n)
    n2=0
    while n>0:
        n2=n2*10+n%10
        n=n//10
    print(n1,n2)
    if n1==n2:
        return True
    else:    
        return False
print(palandrome(12321))

