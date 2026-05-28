def linear_search(arr,search_element):
    for i in range(0,len(arr)):
        if arr[i]==search_element:
            return i
    print("Element not found in the array")
    return -1
arr=[1,2,3,4,5]
print(linear_search(arr,30))
# time complexity is O(n) as we are iterating through the array once and space complexity is O(1) as we are not using any extra space to store the modified array.