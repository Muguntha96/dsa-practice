# Find GCD of two numbers

# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.
# Examples

# Example 1:
# Input: N1 = 9, N2 = 12

# Output: 3
# Explanation:
# Factors of 9: 1, 3, 9
# Factors of 12: 1, 2, 3, 4, 6, 12
# Common Factors: 1, 3
# Greatest common factor: 3 (GCD)
class Solution:
    def GCD(self, n1, n2):
        while n2!=0:
            temp=n1%n2
            n1=n2
            n2=temp
        return n1
sol=Solution()
n1=9
n2=12
print(sol.GCD(n1,n2))