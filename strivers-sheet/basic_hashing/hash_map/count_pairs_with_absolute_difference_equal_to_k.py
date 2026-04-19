# Given an array arr[] and a positive integer k, the task is to count all pairs (i, j) such that i < j and absolute value of (arr[i] - arr[j]) is equal to k. 

# Examples: 

#     Input: arr[] = [1, 4, 1, 4, 5], k = 3
#     Output: 4
#     Explanation: There are 4 pairs with absolute difference 3, the pairs are [1, 4], [1, 4], [1, 4] and [4, 1]

#     Input: arr[] = [8, 16, 12, 16, 4, 0], k = 4
#     Output: 5
#     Explanation: There are 5 pairs with absolute difference 4, the pairs are [8, 12], [8, 4], [16, 12], [12, 16], [4, 0].
from typing import List
class Solution:
    def countAbsoluteDiff(self,arr:List[int],k:int)->int:
        map={}
        count=0
        for i in range(len(arr)):
            if arr[i]-k in map:
                count=count+1
            if arr[i]+k in map:
                count+=1
            map[arr[i]]=i
        print(map)
        return count

sol=Solution()
arr= [8, 16, 12, 16, 4, 0]
k = 4
print(sol.countAbsoluteDiff(arr,k))