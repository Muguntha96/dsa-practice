# Track
# Command Palette

# Search for a command to run...

# Reverse Digits of A Number

# Problem Statement: Given an integer N return the reverse of the given number.

# Note: If a number has trailing zeros, then its reverse will not include them. For e.g , reverse of 10400 will be 401 instead of 00401. 
# Input: N = 12345
# Output:54321
# Explanation: The reverse of 12345 is 54321.

# Input: N = 7789                
# Output: 9877
# Explanation: The reverse of number 7789 is 9877

class Solution:
    def reverseNumber(self, n):
        sign=-1 if n<0 else 1
        n=abs(n)
        res=0
        while n>0:
            rem=n%10
            res=res*10+rem
            n=n//10
        return sign*res
sol=Solution()
n=-7789
print(sol.reverseNumber(n))