# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# Input: n = 4
# 1

# 12

# 123

# 1234

# 12345


# Print the pattern in the function given to you.
class Solution:
    def pattern3(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1,end="")
            print()
sol=Solution()
n=4
sol.pattern3(n)
