# Given an integer array arr[], find the element that appears most frequently. If multiple elements have the same highest frequency, return the largest among them.

# Examples: 

#     Input : arr[] = [1, 3, 2, 1, 4, 1]
#     Output : 1
#     Explanation: 1 appears three times in array which is maximum frequency.

#     Input : arr[] = [10, 20, 10, 20, 30, 20, 20]
#     Output : 20 appears four times in array which is maximum frequency

#     Input: arr[] = [1, 2, 2, 4, 1]
#     Output: 2
#     Explanation: 1 and 2 both appear two times, so return 2 as it's value is bigger.
from typing import List
class Solution:
    def mostFrequentElementinArray(self,a:List[int])->int:
        map={}

        for num in a:
            map[num]=map.get(num,0)+1
        res=None
        max_freq=0
        for num,count in map.items():
            if count>max_freq:
                max_freq=count
                res=num
            if count==max_freq:
                res=max(res,num)
        return res


sol=Solution()
a= [1, 2, 2, 4, 1]
print(sol.mostFrequentElementinArray(a))
