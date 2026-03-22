# You are given an m x n 2-D integer array matrix and an integer target.

#     Each row in matrix is sorted in non-decreasing order.
#     The first integer of every row is greater than the last integer of the previous row.

# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:

# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true

from typing import List


class Solution:
    def search2DMatrix(self,matrix: List[List[int]],target:int)->bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        topRow,bottomRow=0,ROWS-1
        while topRow<=bottomRow:
            mid=(topRow+bottomRow)//2
            if target>matrix[mid][-1]:
                topRow=mid+1
            elif target<matrix[mid][0]:
                bottomRow=mid-1
            else:
                break
        if not (topRow<=bottomRow):
            return False
        l,r=0,COLS-1
        mid=(topRow+bottomRow)//2
        while l<=r:
            mid_idx=(l+r)//2
            if target>matrix[mid][mid_idx]:
                l=mid_idx+1
            elif target<matrix[mid][mid_idx]:
                r=mid_idx-1
            else:
                return True
        return -1
sol=Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
print(sol.search2DMatrix(matrix,target))
