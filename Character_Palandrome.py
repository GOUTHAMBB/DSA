import typing
def character_paladrome_check( s:str)->bool:
    if s==s[-1::-1]:
        return True
    else:
        return False
print(character_paladrome_check("madam"))
# time complexity is O(n) where n is the length of the string and space complexity is O(1) as we are not using any extra space to store the characters of the string.   
def character_paladrome_check_using_recursion(s:str,start: int,end:int)->bool:
    if start>=end:
        return True
    elif s[start]!=s[end]:
        return False
    return character_paladrome_check_using_recursion(s,start+1,end-1)
print(character_paladrome_check_using_recursion("madaam",0,5))
# TC is o(n) where n is the length of the string and space complexity is O(n) as we are using recursion and the maximum depth of the recursion is n/2 in the worst case when the string is of odd length and n/2+1 in the worst case when the string is of even length. 
