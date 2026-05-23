import typing
def insertion_sort(arr: typing.List[int]) -> typing.List[int]:
    for i in range(1, len(arr)): # Start at 1 (first element is "sorted")
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print(insertion_sort([5, 4, 3, 2, 1]))

