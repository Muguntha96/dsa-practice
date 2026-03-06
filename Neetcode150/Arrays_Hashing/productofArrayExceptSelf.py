# Products of Array Except Self
# Medium Topics Company Tags
# Hints

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

# Answer:
from typing import List


class Solution:
    def productofArrayExceptSelf(self,nums:List[int])->List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]*=prefix
            print(res[i])
            prefix*=nums[i]
            print(prefix)
        postfix=1
        # print(range(len(nums)-1,-1,-1))
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            print(res[i])
            postfix*=nums[i]
            print(postfix)
        return res

sol=Solution()
nums=[1,2,4,6]
print(sol.productofArrayExceptSelf(nums))