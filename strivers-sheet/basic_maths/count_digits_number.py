# Problem Statement: Given an integer N, return the number of digits in N. 
# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.

class Solution:
    def countDigit(self, n):
        count=0
        while n>0:
            rem=n%10
            count+=1
            n=n//10
        return count
sol=Solution()
n=1245
print(sol.countDigit(n))