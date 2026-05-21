def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_index=i
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
print(selection_sort([5,4,3,2,1]))
# time complexity is O(n^2) as we are using two nested loops to sort the array and space complexity is O(1) as we are sorting the array in place without using any extra space. 