# Given two arrays a[] and b[], check if they are disjoint, i.e., there is no element common between both the arrays.

# Examples:

#     Input: a[] = [12, 34, 11, 9, 3], b[] = [2, 1, 3, 5] 
#     Output: False
#     Explanation: 3 is common in both the arrays.

#     Input: a[] = [12, 34, 11, 9, 3], b[] = [7, 2, 1, 5] 
#     Output: True 
#     Explanation: There is no common element in both the arrays.
from typing import List


class Solution:
    def checkDisjoint(self,a:List[int],b:List[int])->bool:
        seen=set(a)
        for n in b:
            if n in seen:
                return False
        return True

sol=Solution()
a= [12, 34, 11, 9, 3]
b = [7, 2, 1, 5] 
print(sol.checkDisjoint(a,b))