class Solution:
    def longestConsecutive(self, arr):
        if len(arr)==1:
            return 1
        arr.sort()
        largest_consecutive_sequence=0
        current_consecutive=1
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                if largest_consecutive_sequence<current_consecutive:
                    largest_consecutive_sequence=current_consecutive
                continue
            elif arr[i+1]-arr[i]==1:
                current_consecutive+=1
            else:
                current_consecutive=1
            if largest_consecutive_sequence<current_consecutive:
                largest_consecutive_sequence=current_consecutive
        return largest_consecutive_sequence
    def longestConsecutive_optimal(self, arr):
        if len(arr)==1:
            return 1
        arr_set=set(arr)
        max_sequence=0
        smallest=0
        c=1
        for i in arr_set:
            c=1
            while i+1 in arr_set:
                i=i+1
                print(i)
                c+=1
            if c>max_sequence:
                max_sequence=c
        return max_sequence 
o1=Solution()
print(o1.longestConsecutive_optimal([100,4,200,1,3,2]))
        