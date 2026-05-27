# The question is to move all the zeros in the array to the end of the array while maintaining the relative order of the non-zero elements. The solution is to iterate through the array and whenever we encounter a non-zero element, we move it to the front of the array and keep track of the index of the last non-zero element. After iterating through the array, we fill the remaining elements with zeros.
from pyparsing import nums


def move_the_zeros_to_end_of_the_array_bruteforce(arr):
	for i in range(0,len(arr)):
		if arr[i]==0:
			arr.pop(i)
			arr.append(0)
	return arr
arr=[0,1,0,3,12]
print(move_the_zeros_to_end_of_the_array_bruteforce(arr))
# time complexity is O(n^2) as we are iterating through the array once and for each zero element we are popping it from the array and appending it to the end of the array which takes O(n) time. Space complexity is O(1) as we are not using any extra space to store the modified array.

def move_the_zeros_to_end_of_the_array(arr):
	temp=[]
	zeros=0
	for i in range(0,len(arr)):
		if arr[i]!=0:
			temp.append(arr[i])
			zeros+=1
	for i in range(1,zeros):
		temp.append(0)
	return temp
arr=[0,1,0,3,12]
print(move_the_zeros_to_end_of_the_array(arr))
# time complexity is O(n) as we are iterating through the array once and space complexity is O(n) as we are using an extra array to store the modified array.

def move_the_zeros_to_end_of_the_array_optimized(arr):
        left = 0
        for right in range(len(arr)):
            if arr[right] != 0:
                arr[right], arr[left] = arr[left], arr[right]
                left += 1
        
        return arr

arr=[0,1,0,3,12]
print(move_the_zeros_to_end_of_the_array_optimized(arr))
#time complexity is O(n) and space complexity is O(1) as we are not using any extra space to store the modified array.
		