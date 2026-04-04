# Given a string s, return true if the string is palindrome, otherwise false.


# A string is called palindrome if it reads the same forward and backward.

# Example 1

# Input : s = "hannah"

# Output : true

# Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

# Example 2

# Input : s = "aabbaA"

# Output : false

# Explanation : The string when reversed is --> "Aabbaa", which is not same as original string, So we return false.

class Solution:
    def palidromeRecursion(self,s:str,start:int,end:int)->bool:
        if start>=end:
            return True
        if s[start]!=s[end]:
            return False
        return self.palidromeRecursion(s,start+1,end-1)
    def isPalindromeSinglePointer(self,sStr:str,i:int)->bool:
        if i>=len(sStr)//2:
            return True
        if sStr[i]!=sStr[len(sStr)-i-1]:
            return False
        return self.isPalindromeSinglePointer(sStr,i+1)


sol=Solution()
s = "aabbcccdbbaa"
start=0
end=len(s)-1
print(sol.palidromeRecursion(s,start,end))
sStr="hannah"
print(sol.isPalindromeSinglePointer(sStr,0))