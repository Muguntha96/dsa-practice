from typing import List


class Solution:
    def printSubsequences(self,nums:List[int],i:int,n:List[int])->List[int]:
        if i==len(nums):
            print(n)
            return 
        n.append(nums[i])
        self.printSubsequences(nums,i+1,n)
        n.pop()
        self.printSubsequences(nums,i+1,n)
sol=Solution()
nums=[3,1,2]
n=[]
print(sol.printSubsequences(nums,0,n))