# Given two arrays arr1[] and arr2[] consisting of n and m elements respectively. The task is to find the minimum number of elements to remove from each array such that intersection of both arrays becomes empty and both arrays become mutually exclusive.

# Examples: 

#     Input: arr[] = { 1, 2, 3, 4}, arr2[] = { 2, 3, 4, 5, 8 }
#     Output: 3
#     Explanation: We need to remove 2, 3 and 4 from any array.

#     Input: arr[] = { 4, 2, 4, 4}, arr2[] = { 4, 3 }
#     Output: 1
#     Explanation: We need to remove 4 from arr2[]

#     Input : arr[] = { 1, 2, 3, 4 }, arr2[] = { 5, 6, 7 }
#     Output : 0
#     Explanation: There is no common element in both
from typing import List
class Solution:
    def removeCommon(self,nums1:List[int],nums2:List[int])->int:
        seen=set(nums1)
        count=0
        for num in nums2:
            if num in seen:
                count=count+1
                seen.remove(num)
        return count

sol=Solution()
nums1=[1,2,3,4]
nums2=[2,3,4,5,8]
print(sol.removeCommon(nums1,nums2))

