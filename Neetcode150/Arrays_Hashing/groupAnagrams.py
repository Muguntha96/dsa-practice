# Group Anagrams
# Medium Topics Company Tags
# Hints

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]

# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Answer:
# We have to take array of strings as input and return the output in sublists and it can be ay order
# My approach is using hashmap to group the words based on their pattern
# First,create a hashmap by using collection library default dict
# Then,iterate the array of strings
# Then,Create a list with size of 26 and initialize 0 
# Then iterate the word
# Then check the count list if the character exist  no increment to 1
# then convert the count list to tuple because tuple is immutable
# then append the word and list patttern to hashmap
# Finaly return the hashmap values

from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self,strs:List[str])->List[List[str]]:
        hstr=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord("a")]+=1            
            hstr[tuple(count)].append(word)
        return list(hstr.values())
    
sol=Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs))
