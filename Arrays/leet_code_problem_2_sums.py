class Solution:
    def twoSum(self,arr,target):
        for i in range(0,len(arr)):
            complement=target-arr[i]
            for j in range(i+1,len(arr)):
                if complement==arr[j]:
                    return [i,j]
    def twoSum_optimal(self,arr,target):
        maping={}
        for i in range(0,len(arr)):
            if target-arr[i] in maping and i!=maping[target-arr[i]]:
                return i,maping[target-arr[i]]
            maping[arr[i]]=i
