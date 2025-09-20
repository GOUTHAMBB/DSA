import numpy as np
def count_the_digits(n):
    n=int(n)
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
def count_the_digits2(n):
    n=int(n)
    return int(np.log10(n)+1)
print(count_the_digits2("020303"))
#Time complexity O(log10(n))
#Space complexity O(1)