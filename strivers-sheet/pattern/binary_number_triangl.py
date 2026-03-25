# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# 1 

# 0 1 

# 1 0 1 

# 0 1 0 1 

# 1 0 1 0 1


# Print the pattern in the function given to you.
class Solution:
    def pattern11(self, n):
        for i in range(n):
            start=(i+1)%2
            for j in range(i+1):
                print(start,end="")
                start=1-start
            print()

sol=Solution()
n=5
sol.pattern11(n)