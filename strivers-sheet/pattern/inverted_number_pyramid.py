# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# 12345

# 1234

# 123

# 12

# 1


# Print the pattern in the function given to you.

# Example 1

# Input: n = 4
class Solution:
    def pattern6(self, n):
        for i in range(n,-1,-1):
            for j in range(i):
                print(j+1,end="")
            print()
sol=Solution()
n=4
sol.pattern6(n)