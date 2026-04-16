# Given two arrays, a[] and b[] of equal length. The task is to determine if the given arrays are equal or not. Two arrays are considered equal if:

#     Both arrays contain the same set of elements.
#     The arrangements (or permutations) of elements may be different.
#     If there are repeated elements, the counts of each element must be the same in both arrays.

# Examples: 

#     Input: a[] = [1, 2, 5, 4, 0], b[] = [2, 4, 5, 0, 1]
#     Output: true

#     Input: a[] = [1, 2, 5, 4, 0, 2, 1], b[] = [2, 4, 5, 0, 1, 1, 2] 
#     Output: true

#      Input: a[] = [1, 7, 1], b[] = [7, 7, 1]
#     Output: false
from typing import List
class Solution:
    def checifTwoArraysEqual(self,a:List[int],b:List[int]):
        map={}
        for i in range(len(a)):
            map[a[i]]=map.get(a[i],0)+1
            map[b[i]]=map.get(b[i],0)-1
        for val in map.values():
            if val!=0:
                return False
        return True

sol=Solution()
a = [1, 2, 5, 4, 0, 2, 1]
b= [2, 4, 5, 0, 1, 1, 2] 
print(sol.checifTwoArraysEqual(a,b))