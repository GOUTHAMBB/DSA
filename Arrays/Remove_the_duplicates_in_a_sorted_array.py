def remove_duplicates_using_python_easy_way(arr):
	result=list(set(arr))
	return result
arr=[1,1,2,2,3,4,5,5]
print(remove_duplicates_using_python_easy_way(arr)) 

def removing_duplicates_with_fequency_mapping_brute_force(arr):
    freq_map={}
    for num in range(0,len(arr)):
        freq_map[arr[num]]=0
    print(freq_map)
    i=0
    for k in freq_map.keys():
        arr[i]=k
        i+=1
    return arr[0:i:1]
arr=[1,1,2,2,3,4,5,5]
print(removing_duplicates_with_fequency_mapping_brute_force(arr))
# Time complexity is O(2n) as we are iterating through the array once to create the frequency map and then iterating through the keys of the frequency map to update the original array. Space complexity is O(n) as we are creating a frequency map that can have at most n unique elements in the worst case when all elements in the array are distinct.

def removing_duplicates_optimized(arr):
     i=1
     for j in range(0,len(arr)-1):
         if arr[i]!=arr[j]:
              arr[i]=arr[j]
              i+=1
     return arr[0:i:1]
arr=[1,1,2,2,3,4,5,5]
print(removing_duplicates_optimized(arr))       