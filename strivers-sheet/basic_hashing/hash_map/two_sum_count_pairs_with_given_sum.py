# Given an array arr[] of n integers and a target value, find the number of pairs of integers in the array whose sum is equal to target.

# Examples:  

#     Input: arr[] = [1, 5, 7, -1, 5], target = 6
#     Output:  3
#     Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

#     Input: arr[] = [1, 1, 1, 1], target = 2
#     Output:  6
#     Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1) and (1, 1).

#     Input: arr[] = [10, 12, 10, 15, -1], target = 125
#     Output:  0
#     Explanation: There is no pair with sum = target
from typing import List
class Solution:
    def twoSumCountPairWithSum(self,arr:List[int],target:int)->bool:
        seen=set()
        count=0
        for i in range(len(arr)):
            diff=target-arr[i]
            if diff in seen:
                count=count+1
            seen.add(arr[i])
        return count

sol=Solution()
arr = [10, 12, 10, 15, -1]
target = 125
print(sol.twoSumCountPairWithSum(arr,target))