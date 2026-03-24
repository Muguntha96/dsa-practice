# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


#     *
#    ***
#   *****
#  *******
# *********


# Print the pattern in the function given to you.
class Solution:
    def pattern7(self, n):
        for i in range(1,n+1):
            for j in range(n-i):
                print(" ",end="")
            for k in range(2*i-1):
                print("*",end="")
            print()
sol=Solution()
n=4
sol.pattern7(n)            
