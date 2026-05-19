def reverse_number_with_str_logic(num):
   num=str(num)
   return num[::-1]
print(reverse_number_with_str_logic(1234))
def reverse_number_with_math_logic(num):
   rev=0
   while num>0:
      rev=rev*10+num%10
      num=num//10
   return rev
print(reverse_number_with_math_logic(1234))
