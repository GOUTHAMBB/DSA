def buble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(buble_sort([5,4,3,2,1]))
# time complexity is O(n^2) as we are using two nested loops to sort the array and space complexity is O(1) as we are sorting the array in place without using any extra space. 