# Given two arrays a[] and b[], find their intersection — the unique elements that appear in both. Ignore duplicates, and the result can be in any order.

#     Input: a[] = [1, 2, 1, 3, 1], b[] = [3, 1, 3, 4, 1]
#     Output: [1, 3]
#     Explanation: 1 and 3 are the only common elements and we need to print only one occurrence of common elements

#     Input: a[] = [1, 1, 1], b[] = [1, 1, 1, 1, 1]
#     Output: [1]
#     Explanation: 1 is the only common element present in both the arrays.

#     Input: a[] = [1, 2, 3], b[] = [4, 5, 6]
#     Output: []
#     Explanation: No common element in both the arrays
from typing import List
class Solution:
    def intersectionOfTwoArrays(self,a:List[int],b:List[int])->List[int]:
        aSeen=set(a)
        bSeen=set(b)

        res=[]
        for num in bSeen:
            if num in aSeen:
                res.append(num)
        return res
sol=Solution()
a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]
print(sol.intersectionOfTwoArrays(a,b))
