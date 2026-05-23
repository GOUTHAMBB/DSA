import typing
def insertion_sort(arr: typing.List[int]) -> typing.List[int]:
    for i in range(1, len(arr)): # Start at 1 (first element is "sorted")
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            print(arr)
            j -= 1
        arr[j + 1] = key
        print(arr)
    return arr
print(insertion_sort([5, 4, 3, 2, 1]))

# Time complexity is O(n^2) in the worst case when the array is sorted in reverse order and O(n) in the best case when the array is already sorted. Space complexity is O(1) as we are sorting the array in place without using any extra space.