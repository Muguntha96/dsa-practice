# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. If such a pair exists, return 'Yes', otherwise return 'No'.

# Examples: 

#     Input: k = 3, arr[] = [1, 2, 3, 4, 1, 2, 3, 4]
#     Output: No
#     Explanation: Each element in the given array arr[] appears twice and the distance between every element and its duplicate is 4.

#     Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]
#     Output: Yes
#     Explanation: 1 is present at index 0 and 3.

#     Input: k = 3, arr[] = [1, 2, 3, 4, 5]
#     Output: No
#     Explanation: There is no duplicate element in arr[].
from typing import List
class Solution:
    def dupliateWithinKDistanceinArray(self,arr:List[int],k:int)->bool:
        last_seen={}
        distance=0
        for i,num in enumerate(arr):
            if num in last_seen:
                distance=i-last_seen[num]
                if distance<=k:
                    return True
                
            
            last_seen[num]=i
        return False
sol=Solution()
arr = [1, 2, 3, 4, 1, 2, 3, 4]
k = 3
print(sol.dupliateWithinKDistanceinArray(arr,k))