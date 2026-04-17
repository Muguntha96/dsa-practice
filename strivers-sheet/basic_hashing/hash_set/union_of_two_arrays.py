# Given two arrays a[] and b[], Return union of both the arrays in any order.
# Note: Union of two arrays is an array having all distinct elements that are present in either array.

# Examples:

#     Input : a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
#     Output : [3, 2, 1]
#     Explanation: 3, 2 and 1 are the distinct elements present in either array.

#     Input : a[] = [1, 2, 3], b[] = [4, 5, 6]
#     Output : [1, 2, 3, 4, 5, 6]
#     Explanation: 1, 2, 3, 4, 5 and 6 are the elements present in either array.

from typing import List
class Solution:
    def unionOfTwoArrays(self,a:List[int],b:List[int])->List[int]:
        aSet=set(a)
        for num in b:
            if num not in aSet:
                aSet.add(num)
        return list(aSet)
sol=Solution()
a = [1, 2, 3, 2, 1] 
b= [3, 2, 2, 3, 3, 2]
print(sol.unionOfTwoArrays(a,b))