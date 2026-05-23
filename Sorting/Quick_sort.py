#Quick sort with first element as pivot
def partition_code_f(arr,low,high):
    i=low
    j=high
    pivot=arr[low]
    while i<j:
     while arr[i]<=pivot and i<high:
        i+=1
     while arr[j]>=pivot and j>low:
        j-=1
    if i<j:
     arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quick_sort(arr,low,high):
    if low<high:
        pi=partition_code_f(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
    return arr
print(quick_sort([5,4,3,2,1],0,4))
#Quick sort with last element as pivot
def partition_code_l(arr,low,high):
    i=low
    j=high
    pivot=arr[high]
    while i<j:
     while arr[i]<=pivot and i<high:
        i+=1
     while arr[j]>=pivot and j>low:
        j-=1
    if i<j:
     arr[i],arr[j]=arr[j],arr[i]
    arr[high],arr[i]=arr[i],arr[high]
    return i
# time complexity is O(n log n)  and space complexity is O(1)
#Worst case time complexity is O(n^2) when the array is already sorted or reverse sorted and best case time complexity is O(n log n) when the pivot divides the array into two equal halves.