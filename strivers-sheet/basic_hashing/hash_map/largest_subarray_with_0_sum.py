# Given an array arr[] consisting of both positive and negative integers, find the length of the longest subarray whose elements sum is zero.
# A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.

# Examples:

#     Input: arr[] = [15, -2, 2, -8, 1, 7, 10]
#     Output: 5
#     Explanation: The longest subarray with sum equals to 0 is [-2, 2, -8, 1, 7].

#     Input: arr[] = [1, 2, 3]
#     Output: 0
#     Explanation: There is no subarray with 0 sum.

#     Input:  arr[] = [1, 0, 3]
#     Output:  1
#     Explanation: The longest sub-array with sum equal to 0 is [0]z
from typing import List
class Solution:
    def largestSubArraywithzeroSum(self,nums:List[int])->int:
        seen={}
        maxLen=0
        prefix=0
        i=0
        while i<len(nums):
            prefix+=nums[i]
            if prefix==0:
                maxLen=max(maxLen,i+1)
            if prefix in seen:
                maxLen=i-seen[prefix]
            else:
                seen[prefix]=i
            i+=1
        return maxLen

sol=Solution()
nums=[1, 0, 3]
print(sol.largestSubArraywithzeroSum(nums))