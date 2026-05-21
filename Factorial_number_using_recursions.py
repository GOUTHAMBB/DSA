#function recursion
def factorial_using_recursion_using_function_recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_using_recursion_using_function_recursion(n-1)
#parameterised recursion
def factorial_using_parameterised_recursion(n,i):
    if n==0 or n==1:
        return 1
    elif i==1:
        return 1
    return n*factorial_using_parameterised_recursion(n-1,i-1)

print(factorial_using_recursion_using_function_recursion(5))
print(factorial_using_parameterised_recursion(1,1))