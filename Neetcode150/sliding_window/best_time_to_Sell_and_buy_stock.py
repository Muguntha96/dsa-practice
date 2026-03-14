# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        l,r=0,1
        while r<len(prices):
            if prices[l]<prices[r]:
                currprof=prices[r]-prices[l]
                p=max(p,currprof)
            else:
                l=r
            r+=1
        return p
sol=Solution()
prices = [10,1,5,6,7,1]
print(sol.maxProfit(prices))