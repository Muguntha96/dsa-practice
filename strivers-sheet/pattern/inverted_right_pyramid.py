# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# *****

# ****

# ***

# **

# *


# Print the pattern in the function given to you.

# Example 1

# Input: n = 4
class Solution:
    def pattern5(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end="")
            print()
sol=Solution()
n=4
sol.pattern5(n)