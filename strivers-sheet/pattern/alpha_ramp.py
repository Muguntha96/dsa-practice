# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# A

# BB

# CCC

# DDDD

# EEEEE


# Print the pattern in the function given to you.
class Solution:
    def pattern16(self, n):
        val=64
        for i in range(n):
            val+=1
            for j in range(i+1):
                print(chr(val),end="")
            print()
            
sol=Solution()
n=4
sol.pattern16(n)