# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true


# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false
# Answer:
    # create a hashset
    # iterate the array
    # check the number in hashset
    # if the number exist return true
    # if not add the number to set
    # time complexity is o(n)
from typing import List  #
class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

sol = Solution()
nums = [1, 2, 3, 3]
print(sol.hasDuplicate(nums))