# Given an array arr[] of size n, let min and max be the minimum and maximum elements in the array respectively. Find how many numbers should be added so that every element in the range [min, max] occurs at least once in the array.

# Examples:  

#     Input : arr[] = [4, 5, 3, 8, 6]
#     Output : 1
#     Explanation: Range is 3-8; only 7 is missing, so count = 1.

#     Input : arr[] = [2, 1, 3]
#     Output : 0
#     Explanation: Range is 1-3; no elements are missing, so count = 0.
from typing import List
class Solution:
    def findMissingCountMinToMax(self,arr:List[int])->int:
        seen=set()
        maxi=float('-inf')
        mini=float('inf')
        for n in arr:
            seen.add(n)
            if n<mini:
                mini=n
            if n>maxi:
                maxi=n
        return (maxi-mini+1)-len(seen)

sol=Solution()
arr= [2, 1, 3]
print(sol.findMissingCountMinToMax(arr))