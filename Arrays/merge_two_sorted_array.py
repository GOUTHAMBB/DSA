def merge_2_sorted_arrays(arr1,arr2):
    i=k=j=0
    merged_array=[]
    if len(arr1)>=len(arr2):
        while i<len(arr1):
            while k!=0  and i<len(arr1) and arr1[i]==merged_array[k-1]:
                i+=1
            while k!=0  and j<len(arr2) and arr2[j]==merged_array[k-1]:
                j+=1
            if j<len(arr2) and arr1[i]<arr2[j]:
                merged_array.append(arr1[i])
                i+=1
            elif j<len(arr2) :
                merged_array.append(arr2[j])
                j+=1
            else: 
                merged_array.append(arr1[i])
                i+=1
            k+=1
    else:
        while i<len(arr2):
            while k!=0 and i<len(arr2) and arr2[i]==merged_array[k-1]:
                i+=1
            while k!=0  and j<len(arr1) and arr1[j]==merged_array[k-1]:
                j+=1
            if j<len(arr1) and arr2[i]<arr1[j]:
                merged_array.append(arr2[i])
                i+=1
            elif j<len(arr1) :
                merged_array.append(arr1[j])
                j+=1
            else: 
                merged_array.append(arr2[i])
                i+=1
            k+=1
    return merged_array
    
print(merge_2_sorted_arrays([1,1,2,3,3,4],[1,2,3,3]))
print(merge_2_sorted_arrays([1,2,3,3],[1,1,2,3,3,4]))

def merge_2_sorted_array_optimised(arr1,arr2):
    i=j=0
    merged_array=[]
    def append_unique(element):
        if len(merged_array)==0:
            merged_array.append(element)
        elif merged_array[-1]!=element:
            merged_array.append(element)
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            append_unique(arr1[i])
            i+=1
        elif  arr2[j]<arr1[i]:
            append_unique(arr2[j])
            j+=1
        else:
            append_unique(arr1[i])
            i+=1
            j+=1
    while i<len(arr1):
        append_unique(arr1[i])
        i+=1
    while j<len(arr2):
        append_unique(arr2[j])
        j+=1
    return merged_array
print(merge_2_sorted_array_optimised([1,1,2,3,3,4],[1,2,3,3]))
print(merge_2_sorted_array_optimised([1,2,3,3],[1,1,2,3,3,4]))
# Time complexity: O(m+n) where m and n are the lengths of the two arrays
# Space complexity: O(m+n) in the worst case when there are no duplicates and all elements are unique. However, in the best case when all elements are duplicates, the space complexity is O(1) as only one element will be stored in the merged array.

        
        