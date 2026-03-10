# You are given an integer array heights where heights[i] represents the height of the ithith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        left=0
        right=len(height)-1
        while left<right:
            w=right-left
            val=min(height[left],height[right])
            a=w*val
            if a> res:
                res=a
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res
    
sol=Solution()
height=[1,7,2,5,4,7,3,6]
print(sol.maxArea(height))