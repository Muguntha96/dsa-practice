# You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.


# A palindrome number is a number which reads the same both left to right and right to left.

# Example 1

# Input: n = 121

# Output: true

# Explanation: When read from left to right : 121.

# When read from right to left : 121.

# Example 2

# Input: n = 123

# Output: false

# Explanation: When read from left to right : 123.

# When read from right to left : 321.

class Solution:
    def isPalindrome(self, n):
        original=n
        res=0
        while n>0:
            rem=n%10
            res=res*10+rem
            n=n//10
        return res==original
sol=Solution()
n=121
print(sol.isPalindrome(n))