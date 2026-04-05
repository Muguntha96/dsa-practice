# Count frequency of each element in the array

# Problem Statement: Given an array, we have found the number of occurrences of each element in the array.
# Examples

# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
# 	            5  2
#                 15  1
# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array
from typing import List


class Solution:
    def freqEachElement(self,nums:List[int]):
        freq={}
        for num in nums:
            freq[num]=1+freq.get(num,0)
        output = [[num, count] for num, count in freq.items()]
        return output
sol=Solution()
nums=[10,5,10,15,10,5]
print(sol.freqEachElement(nums))
        