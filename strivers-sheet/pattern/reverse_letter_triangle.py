# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# ABCDE

# ABCD

# ABC

# AB

# A


# Print the pattern in the function given to you.

class Solution:
    def pattern15(self, n):
        for i in range(n,-1,-1):
            val=65
            for j in range(i):
                print(chr(val),end="")
                val+=1
            print()
sol=Solution()
n=4
sol.pattern15(n)