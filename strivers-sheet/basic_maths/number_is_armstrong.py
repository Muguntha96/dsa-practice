# Check if the Number is Armstrong

# Subscribe to TUF+

# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.


# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

# Example 1

# Input: n = 153

# Output: true

# Explanation: Number of digits : 3.

# 13 + 53 + 33 = 1 + 125 + 27 = 153.

# Therefore, it is an Armstrong number.
class Solution:
    def isArmstrong(self, n):
        if n==0:
            return True
        org=n
        count=len(str(n))
        res=0
        while n>0:
            rem=n%10
            res+=rem**count
            n=n//10
        return res==org
sol=Solution()
n=12
print(sol.isArmstrong(n))
