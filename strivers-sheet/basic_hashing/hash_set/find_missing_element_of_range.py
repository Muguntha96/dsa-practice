# Given an array, arr[0..n-1] of distinct elements and a range [low, high], find all numbers that are in a range, but not the array. The missing elements should be printed in sorted order.

# Examples:  

#     Input: arr[] = {10, 12, 11, 15}, 
#            low = 10, high = 15
#     Output: 13, 14

#     Input: arr[] = {1, 14, 11, 51, 15}, 
#            low = 50, high = 55
#     Output: 50, 52, 53, 54 55
from typing import List
class Solution:
    def findMissingEle(self,arr:List[int],low:int,high:int):
        seen=set(arr)
        res=[]
        for i in range(low,high+1):
            if i not in seen:
                res.append(i)
        return (",".join(map(str,res)))

sol=Solution()
arr = [10, 12, 11, 15]
low=10
high=15
print(sol.findMissingEle(arr,low,high))
