def frequency_mapping_in_dictionary1(l1):
    dict1=dict()
    for i in l1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    return dict1
#time complexity is O(n)
#space complexity is O(k) where k is the number of unique elements in the list worst case is O(n)
def frequency_mapping_in_dictionary2(l1):
    n=len(l1)
    dict1=dict()
    for i in range(0,n):
        dict1[l1[i]]=dict1.get(l1[i],0)+1
    return dict1
print(frequency_mapping_in_dictionary1([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1, 2,3,4,5,1,2,3,4,5]))
print(frequency_mapping_in_dictionary2([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1, 2,3,4,5,1,2,3,4,5]))   