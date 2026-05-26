def left_rotate_arr_list_slicing(arr,k):
    arr=arr[k:len(arr)]+arr[0:k]
    return arr
def left_rotate_arr_list_method(arr,k):
    for i in range(1,k+1):
        arr.insert(len(arr),arr[0])
        arr.pop(0)
    return arr
arr=[1,2,3,4,5]
print(left_rotate_arr_list_slicing(arr,2))
print(left_rotate_arr_list_method(arr,2))

# time complexity is O(n*k) as we are iterating through the array k times and space complexity is O(1) as we are not using any extra space to store the rotated array.


def right_rotate_arr_list_slicing(arr,k):
    arr=arr[-k:len(arr)]+arr[0:-k]
    return arr
def right_rotate_arr_list_method(arr,k):
    for i in range(1,k+1):
        last_element= arr.pop(len(arr)-1)
        arr.insert(0,last_element)
    return arr
arr=[1,2,3,4,5]
print(right_rotate_arr_list_slicing(arr,2))
print(right_rotate_arr_list_method(arr,2))