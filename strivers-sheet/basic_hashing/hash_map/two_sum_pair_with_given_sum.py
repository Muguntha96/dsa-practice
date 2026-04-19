# Two Sum - Pair with given Sum
# Last Updated : 26 Jul, 2025

# Given an array arr[] of n integers and a target value, check if there exists a pair whose sum equals the target. This is a variation of the 2-Sum problem.

# Examples: 

#     Input: arr[] = [0, -1, 2, -3, 1], target = -2
#     Output: true
#     Explanation: There is a pair (1, -3) with the sum equal to given target, 1 + (-3) = -2.

#     Input: arr[] = [1, -2, 1, 0, 5], target = 0
#     Output: false
#     Explanation: There is no pair with sum equals to given target.
from typing import List
class Solution:
    def twoSumPairWithSum(self,arr:List[int],target:int)->bool:
        map={}
        for i,n in enumerate(arr):
            diff=target-n
            if diff in map:
                return True
            map[n]=i
        return False

sol=Solution()
arr= [1, -2, 1, 0, 5]
target = 0
print(sol.twoSumPairWithSum(arr,target))