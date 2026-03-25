# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


# Print the pattern in the function given to you.
class Solution:
    def pattern19(self, n):
        for i in range(n,0,-1):
            for j in range(i):
                print("*",end="")
            for k in range(2*(n-i)):
                print(" ",end="")
            for p in range(i):
                print("*",end="")
            print()
        for a in range(1,n+1):
            for b in range(a):
                print("*",end="")
            for c in range(2*(n-a)):
                print(" ",end="")
            for d in range(a):
                print("*",end="")
            print()
sol=Solution()
n=4
sol.pattern19(n)