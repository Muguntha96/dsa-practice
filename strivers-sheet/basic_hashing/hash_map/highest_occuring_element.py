# Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.


# Please note that this section might seem a bit difficult without prior knowledge on what hashing is, we will soon try to add basics concepts for your ease! If you know the concepts already please go ahead to give a shot to the problem. Cheers!

# Example 1

# Input: nums = [1, 2, 2, 3, 3, 3]

# Output: 3

# Explanation: The number 3 appears the most (3 times). It is the most frequent element.
class Solution:
    def mostFrequentElement(self, nums):
        freq={}
        res=0
        max=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,val in freq.items():
            if val>max:
                max=val
                res=key
            elif val==max and key<res:
                res=key
                
        
        return res


sol=Solution()
nums = [1, 4,4,4 ,2, 3, 3, 3]
print(sol.mostFrequentElement(nums))