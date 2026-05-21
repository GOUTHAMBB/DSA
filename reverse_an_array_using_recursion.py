[1,2,3,4,5]
def reverse_an_array(arr):
    temp_arr=arr[-1::-1]
    return temp_arr
print(reverse_an_array([1,2,3,4,5]))

def reverse_an_array_using_same_array(arr):
    length=len(arr)
    for i in range(0,length//2):
        arr[i],arr[length-i-1]=arr[length-i-1],arr[i]
    return arr
print(reverse_an_array_using_same_array([1,2,3,4,5]))

def reversing_an_array_using_recursion(arr,start,end):
    if start>=end:
        return
    arr[start],arr[end]=arr[end],arr[start]
    reversing_an_array_using_recursion(arr,start+1,end-1)
    return arr
print(reversing_an_array_using_recursion([1,2,3,4,5],0,4))
# time complexity is O(n) where n is the number of elements in the array
# space complexity is O(n) as we are using recursion and the maximum depth of the recursion is n/2 in the worst case when the array is of odd length and n/2+1 in the worst case when the array is of even length.