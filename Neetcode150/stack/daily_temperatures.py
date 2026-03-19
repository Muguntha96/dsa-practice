# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Example 1:

# Input: temperatures = [30,38,30,36,35,40,28]

# Output: [1,4,1,2,1,0,0]

from typing import List


class Solution():
    def dailyTemperatures(self,temperatures:List[int])->List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_idx=stack.pop()
                ans[prev_idx]=i-prev_idx
            stack.append(i)
        return ans
sol=Solution()
temperatures = [30,38,30,36,35,40,28]
print(sol.dailyTemperatures(temperatures))