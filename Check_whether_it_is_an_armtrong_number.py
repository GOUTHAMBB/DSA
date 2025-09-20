import numpy as np
def armstrong_number_check(num):
    num1=int(num)
    num2=0
    power=count_the_digits2(num)
    while num>0:
        num2=num2+(num%10)**power
        num=num//10
    if num1==num2:
        return True
    else:    
        return False
def armstrong_number_check2(n):
    num=str(n)
    len=len(num)
    while num>0:
        sum=sum+(num%10)**len
        num=num//10
    if sum==str(n):
        return True
    else:    
        return False
def count_the_digits2(n):
    n=int(n)
    return int(np.log10(n)+1)
print(armstrong_number_check(1534))