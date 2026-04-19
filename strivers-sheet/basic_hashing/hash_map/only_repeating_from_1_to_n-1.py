# Given an array arr[] of size n filled with numbers from 1 to n-1 in random order. The array has only one repetitive element. The task is to find the repetitive element.

# Examples:

#     Input: arr[] = [1, 3, 2, 3, 4]
#     Output: 3
#     Explanation: The number 3 is the only repeating element.

#     Input: arr[] = [1, 5, 1, 2, 3, 4]
#     Output: 1
#     Explanation: The number 1 is the only repeating element.
from typing import List
class Solution:
    def onlyRepeating(self,arr:List[int])->int:
        slow=fast=0
        while True:
            slow=arr[slow]
            fast=arr[arr[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow=arr[slow]
            slow2=arr[slow2]
            if slow==slow2:
                return slow

sol=Solution()
arr=[1,3,4,2,2]
print(sol.onlyRepeating(arr))