# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in O(log(m+n))O(log(m+n)) time.

# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0

# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:

# Input: nums1 = [1,3], nums2 = [2,4]

# Output: 2.5
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newlist = nums1 + nums2
        newlist.sort()
        
        n = len(newlist)
        
        if n % 2 == 0:
            return (newlist[n//2 - 1] + newlist[n//2]) / 2
        else:
            return newlist[n//2]
sol=Solution()
nums1 = [1,2]
nums2 = [3]
print(sol.findMedianSortedArrays(nums1,nums2))