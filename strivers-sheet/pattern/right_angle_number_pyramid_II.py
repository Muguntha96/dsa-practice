# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# 1

# 22

# 333

# 4444

# 55555


# Print the pattern in the function given to you.

# Example 1

# Input: n = 4
class Solution:
    def pattern4(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1,end="")
            print()
sol=Solution()
n=4
sol.pattern4(n)