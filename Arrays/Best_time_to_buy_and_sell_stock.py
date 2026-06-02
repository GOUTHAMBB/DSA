
from typing import List

class Solution:
    def maxProfit_not_optimised(self, arr: List[int]) -> int:
        max_profit=0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                current_profit=arr[j]-arr[i]
                if current_profit>0 and max_profit<current_profit:
                    max_profit=current_profit
        return max_profit
    def maxProfit(self, arr: List[int]) -> int:
        min_price_seen_so_far=float('inf')
        max_profit=0
        for i in range(0,len(arr)):
            if arr[i]<min_price_seen_so_far:
                min_price_seen_so_far=arr[i]
                continue
            if max_profit<(arr[i]-min_price_seen_so_far):
                max_profit=arr[i]-min_price_seen_so_far
        return max_profit
        