# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3

# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1


from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # mp={}
        # l=0
        # longest=0
        # for r in range(len(s)):
        #     if s[r] in mp:
        #         l=max(mp[s[r]]+1,l)
        #     mp[s[r]]=r
        #     longest=max(longest,r-l+1)
        # return longest
        charSet=set()
        l=0
        longest=0
        for r in range(len(s)):
            if s[r] in charSet:
                charSet.remove(s[r])
                l+=1
            charSet.add(s[l])
            longest=max(longest,r-l+1)
        return longest
sol=Solution()
s = "zxyzxyz"
    
print(sol.lengthOfLongestSubstring(s))