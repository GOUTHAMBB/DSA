from typing import List
class Solution:
    def rearrangeArray_bruteforce(self, arr: List[int]) -> List[int]:
        positive=[]
        negative=[]
        result=[]
        for i in range(0,len(arr)):
            if arr[i]>0:
                positive.append(arr[i])
            else:
                negative.append(arr[i])
        for i in range(0,len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        n=1
        p=0
        result=[0]*len(arr)
        for i in range(0,len(arr)):
            if arr[i]>0:
                result[p]=arr[i]
                p+=2
            else:
                result[n]+=arr[i]
                n+=2
        return result



        