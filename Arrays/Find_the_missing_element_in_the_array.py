def missing_element_in_array(arr):
    n=len(arr)-1
    j=0
    for i in range(0,n+1):
        if j not in arr:
            arr.append(j)
            return arr
        j+=1
    return arr
print(missing_element_in_array([0,3,1]))
#Time complexity is O(n^2) and space complexity is O(1)
def missing_element_in_array2(arr):
    n=len(arr)
    temp_arr=[0]*n
    for i in range(0,n):
        temp_arr[i]=1
    for i in range(0,n):
        if temp_arr[i]==0:
            arr.append(i)
            return arr
    return arr
print(missing_element_in_array([0,3,1]))
# Time complexity is O(2n) and space complexity is O(n)
def missing_element_in_array_optimal(arr):
    n=len(arr)
    sum=(n*(n+1))/2
    current_sum=0
    for i in range(0,n):
        current_sum+=arr[i]
    missing_element=sum-current_sum
    arr.append(missing_element)
    return arr
print(missing_element_in_array_optimal([0,3,1]))
# Time complexity is O(n) and space complexity is O(1)