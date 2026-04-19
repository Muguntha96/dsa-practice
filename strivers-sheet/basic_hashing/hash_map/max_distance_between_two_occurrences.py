# Given an array arr[], the task is to find the maximum distance between two occurrences of any element. If no element occurs twice, return 0.

# Examples:  

#     Input: arr = [1, 1, 2, 2, 2, 1]
#     Output: 5
#     Explanation: distance for 1 is: 5-0 = 5, distance for 2 is: 4-2 = 2, So max distance is 5.

#     Input : arr[] = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
#     Output: 10
#     Explanation : Max distance for 2 is 11-1 = 10, max distance for 1 is 4-2 = 2 and max distance for 4 is 10-5 = 5  

#     Input: arr[] = [1, 2, 3, 6, 5, 4]
#     Output: 0
#     Explanation: No element has two occurrence, so maximum distance = 0.
from typing import List
class Solution:
    def maxDistaneBetweenTwoOccurrunces(self,arr:List[int])->int:
        first_seen={}
        
        max_distance=0
        for i,num in enumerate(arr):
            if num not in first_seen:
                first_seen[num]=i
            else:
                max_distance=max(max_distance,i-first_seen[num])
        print(first_seen)
        return max_distance
sol=Solution()
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
print(sol.maxDistaneBetweenTwoOccurrunces(arr))
