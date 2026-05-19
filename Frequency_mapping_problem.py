'''
Calculate the number of times the occurance of each element in list1 is present in list2 and return the result in the form of a dictionary.
The following are the constains:
1. The distinct numbers in List1 are 0<n<=10
2. The number of elemnts in List 2 can be 1to 10^8
2. The number of elemnts in List 1 can be 1to 10^8
'''

#Brute force approach
def hash_map_calculator(list1,list2):
    temp={}
    list2=list(set(list2))
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i]==list2[j]:
                if list1[i] in temp:
                    temp[list1[i]]+=1
                else:
                    temp[list1[i]]=1
    return temp
print(hash_map_calculator([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1, 2,3,4,5],[1,2,3,4,5]))

# time complexity is O(n*m) where n is the number of elements in list1 and m is the number of elements in list2
# space complexity is O(k) where k is the number of unique elements in list1 worst case is O(n)
# optimized approach
def hash_map_calculator2(list1,list2):
    temp={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
    for i in range(0,len(list2)):
        if list2[i] in temp:
            temp[list2[i]]+=1
    return temp
print(hash_map_calculator2([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1, 2,3,4,5],[1,2,3,4,5]))
# time complexity is O(m) where m is the number of elements in list2
# space complexity is O(1) as the size of the dictionary is constant
    