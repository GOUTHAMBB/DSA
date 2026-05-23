def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr
print(merge_sort([5, 4, 3, 2, 1]))

# time complexity is O(n log2(n)) as we are dividing the array into two halves and sorting each half recursively and space complexity is O(n) as we are using extra space to store the left and right halves of the array during the merge process.
# best case TC is o(nlog2n)