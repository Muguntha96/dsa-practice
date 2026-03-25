# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


# Print the pattern in the function given to you
class Solution:
    def pattern20(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            for k in range(2*(n-i)):
                print(" ",end="")
            for l in range(i):
                print("*",end="")
            print()
        for p in range(n-1,0,-1):
            for q in range(p):
                print("*",end="")
            for r in range(2*(n-p)):
                print(" ",end="")
            for s in range(p):
                print("*",end="")            

            print()

sol=Solution()
n=4
sol.pattern20(n)