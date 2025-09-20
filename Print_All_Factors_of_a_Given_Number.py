def factors(n):
    num=int(n)
    factors=[]
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    return factors
#time complexoty is O(n)
#space complexity is O(k) and k is the number of factors
def factors2(n):
    num=int(n)
    factors=[]
    for i in range(1,num//2):
        if num%i==0:
            factors.append(i)
    factors.append(num)
    return factors
#time complexoty is O(n/2) which is approximately O(n)
#space complexity is O(k) and k is the number of factors
def factors3(n):
    num=int(n)
    factors=[]
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            factors.append(i)
            if i!=num//i:
                factors.append(num//i)
    factors.sort()
    return factors
#time complexoty is O(sqrt(n))+ O(NlogN)  ehre  O(NlogN) is for sorting
#space complexity is O(k) and k is the number of factors
print(factors(12))