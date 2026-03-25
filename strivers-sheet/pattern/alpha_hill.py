# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA


# Print the pattern in the function given to you.

# Example 1

# Input: n = 4
class Solution:
    def pattern17(self, n):
        val=65
        for i in range(0,n-1):
            for j in range(n-i-1):
                print(" ",end="")
            for k in range(i+1):
                print(chr(65+k),end="")
            for k in range(i-1,-1,-1):
                print(chr(65+k),end="")
            
            print()
sol=Solution()
n=4
sol.pattern17(n)