class Solution:
    def maxSubArray(self, arr):
        max_sum=0
        for i in range(0,len(arr)):
            sum=0
            for j in range(i,len(arr)):
                sum+=arr[j]
            print(f"First window sum:{sum},maxsum:{max_sum},i:{i}")
            if max_sum<sum:
                max_sum=sum
            sum=0
            for j in range(0,len(arr)-i,-1):
                sum+=arr[j]
            print(f"Second window sum:{sum},maxsum:{max_sum},i:{i}")
            if max_sum<sum:
                max_sum=sum
            print(max_sum)
        return max_sum
        
o1=Solution()
print(o1.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
