#Question Calculate the sum of the digits
def sum_of_digits(n):
    sum=0
    while(n>0):
        sum+=n%10
        n=n//10
    return sum
print(sum_of_digits(1221))
#Time complexity O(log10(n))
#Space complexity O(1)