# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

from typing import List


class Solution:
    def reverseArray(self,n:List[int],start:int,end:int)->List[int]:
        if start>=end:
            return n
        temp=n[start]
        n[start]=n[end]
        n[end]=temp
        return self.reverseArray(n,start+1,end-1)


sol=Solution()
n=[5,4,3,2,1]
start=0
end=len(n)-1
print(sol.reverseArray(n,start,end))