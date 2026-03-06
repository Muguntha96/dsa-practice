# Two Sum
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]

# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]

# Constraints:

#     2 <= nums.length <= 1000
#     -10,000,000 <= nums[i] <= 10,000,000
#     -10,000,000 <= target <= 10,000,000
#     Only one valid answer exists.
# Answer:
    # we have to return the indices so we need hashmap to store the number as key and index as value
    # First I create a hash map
    # then iterate the array
    # then find the difference by target-current number
    # chck the diiference in hasmap if exist return the current idx,hashmap value
    # if it dose add the current numebr and idx to the hashmap
    # Time complexity o(n) it will iterate each number in list  and space o(n)--hashmap stores upto n numbers
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in count:
                return [count[diff],i]
            count[num]=i

sol=Solution()
nums = [2,7,11,15]
target = 9
print(sol.twoSum(nums,target))
