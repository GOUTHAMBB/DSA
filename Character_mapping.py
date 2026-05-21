def character_hashing(s1,l1):
    result_list=[0]*123
    dict1=dict()
    for i in range(0,len(s1)):
        result_list[ord(s1[i])]+=1
    for i in range(0,len(l1)):
        dict1[l1[i]]=result_list[ord(l1[i])]
    return dict1
print(character_hashing("hello world",["h","e","l","o","w","r","d"]))
# time complexity is O(n+m) where n is the length of the string s1 and m is the length of the list l1
# space complexity is O(1) 