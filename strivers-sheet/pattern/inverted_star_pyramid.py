# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# *********
#  *******
#   *****
#    ***
#     *


# Print the pattern in the function given to you.

# Example 1

# Input: n = 4
class Solution:
    def pattern8(self, n):
        for i in range(n,0,-1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(2*i-1):
                print("*",end="")
            print()
sol=Solution()
n=4
sol.pattern8(n)    