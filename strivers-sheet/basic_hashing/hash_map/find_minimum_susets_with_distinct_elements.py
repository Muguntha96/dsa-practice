# You are given an array of n-element. You have to make subsets from the array such that no subset contain duplicates. Find out minimum number of subset possible.

# Examples : 

#     Input : arr[] = {1, 2, 3, 4}
#     Output :1
#     Explanation : A single subset can contains all values and all values are distinct.

#     Input : arr[] = {1, 2, 3, 3}
#     Output : 2
#     Explanation : We need to create two subsets {1, 2, 3} and {3} [or {1, 3} and {2, 3}] such that both subsets have distinct elements.
from typing import List
class Solution:
    def findSbsets(self,nums:List[int])->int:
        count=0

        frq={}
        for num in nums:
            frq[num]=frq.get(num,0)+1
        for val in frq.values():
            if count<val:
                count=val

        return count

sol=Solution()
nums=[1,2,3,4]
print(sol.findSbsets(nums))