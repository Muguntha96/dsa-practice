# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

from typing import List


class Solution:
    def reverseArray(self,n:List[int],l:int,r:int)->List[int]:
        if l>=r:
            return n
        n[l],n[r]=n[r],n[l]
        return self.reverseArray(n,l+1,r-1)
    def reverseArraySinglePointer(self,nums:List[int],i:int)->List[int]:
        if i>=len(nums)//2:
            return nums
        nums[i],nums[len(nums)-i-1]=nums[len(nums)-i-1],nums[i]
        return self.reverseArraySinglePointer(nums,i+1)


sol=Solution()
n=[5,4,3,2,1]
nums=[10,20,30,40]
l=0
i=0
r=len(n)-1
print(sol.reverseArray(n,l,r))
print(sol.reverseArraySinglePointer(nums,i))