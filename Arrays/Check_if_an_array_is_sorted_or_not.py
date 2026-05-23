def arr_is_sorted_or_not_python_easy_way(arr):
	arr2=arr.copy()
	arr2.sort()
	if arr==arr2:
		return True
	else:
		return False
def arr_is_sorted_or_not(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(arr_is_sorted_or_not([1,2,3,4,5]))
print(arr_is_sorted_or_not_python_easy_way([1,2,3,4,5]))