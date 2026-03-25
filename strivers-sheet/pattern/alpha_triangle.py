# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# E 

# D E 

# C D E 

# B C D E 

# A B C D E


# Print the pattern in the function given to you.
class Solution:
    def pattern18(self, n):
        for i in range(n):
            for ch in range(ord('A')+n-1-i,ord('A')+n):
                print(chr(ch),end="")
            print()
sol=Solution()
n=5
sol.pattern18(n)