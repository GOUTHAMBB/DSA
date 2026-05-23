def second_largest_element_in_an_array_easy_python_way(arr):
	arr.sort()
	return(arr[-2])
# time complexity is O(n log n) as we are sorting the array and space complexity is O(1) as we are sorting the array in place without using any extra space.
def second_largest_element_in_an_array(arr):
	largest=arr[0]
	second_largest=arr[0]
	for i in range(1,len(arr)):
		if arr[i]>largest:
			largest=arr[i]
	for i in range(1,len(arr)):
		if arr[i]>second_largest and arr[i]!=largest:
			second_largest=arr[i]
	return second_largest
# time complexity is O(2n) as we are traversing the array twice and space complexity is O(1) as we are using only two variables to store the largest and second largest elements.
def second_largest_element_in_an_array_optimal(arr):
	largest=arr[0]
	second_largest=arr[0]
	for i in range(1,len(arr)):
		if arr[i]>largest:
			second_largest=largest
			largest=arr[i]
		elif arr[i]>second_largest and arr[i]!=largest:
			second_largest=arr[i]
	return second_largest
# time complexity is O(n) as we are traversing the array only once and space complexity is O(1) as we are using only two variables to store the largest and second largest elements.
print(second_largest_element_in_an_array([1,2,3,4,5]))
print(second_largest_element_in_an_array_easy_python_way([1,2,3,4,5]))
print(second_largest_element_in_an_array_optimal([1,2,3,4,5]))
