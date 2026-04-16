# Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.

# Examples: 

#     Input: a[] = [11, 1, 13, 21, 3, 7], b[] = [11, 3, 7, 1] 
#     Output: true

#     Input: a[]= [1, 2, 3, 4, 5, 6], b = [1, 2, 4] 
#     Output: true

#     Input: a[] = [10, 5, 2, 23, 19], b = [19, 5, 3] 
#     Output: false
from typing import List


class Solution:
    def checkSubset(slef,a:List[int],b:List[int])->bool:
        checkSubset=set(a)
        for num in b:
            if num not in checkSubset:
                return False
        return True

sol=Solution()
a=[10, 5, 2, 23, 19]
b = [19, 5, 3]
print(sol.checkSubset(a,b))        
        