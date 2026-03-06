# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Answer:
    # angram: two string character should same any order but length and character should be same
    # check both string length if not same return
    # create 2 hashmaps for both strings
    # iterante the loop with length
    # check the hashmap the character exist if not add increase the count to 1
    # Finally check the length of both hashmap if it same return true else fasle
    # i create three logics and all time complexity is 0(n+m) becausewe traverse  all the characters of both string once
    # s str=o(n) t str= o(m)==> o(n+m)
    # all the three solutions i sed extra space eiher create an list or map so it takes O(1) space

class Solution:
    def validAnagram(self,s:str,t:str)->bool:
        if len(s)!=len(t):
            return False
        # sMap,tMap={},{}
        # for idx in range(len(s)):
        #     sMap[idx]=sMap.get(s[idx],0)+1
        #     tMap[idx]=tMap.get(t[idx],0)+1
        # return sMap==tMap
        # count=[0]*26
        # for idx in range(len(s)):
        #     count[ord(s[idx])-ord("a")]+=1
        #     count[ord(t[idx])-ord("a")]-=1
        # for val in count:
        #     if val!=0:
        #         return False
        # return True
        count={}
        for idx in range(len(s)):
            count[s[idx]]=count.get(s[idx],0)+1
            count[t[idx]]=count.get(t[idx],0)-1
        for v in count.values():
            if v!=0:
                return False
        return True
        
        

        

sol=Solution()
s, t = "racecar", "carrace"
print(sol.validAnagram(s,t))