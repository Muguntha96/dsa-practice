# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# *****
# *   *
# *   *
# *   *
# *****


# Print the pattern in the function given to you.
class Solution:
    def pattern21(self, n):
        for i in range(n):
                if i==0 or i==n-1:
                    for j in range(n):
                        print("*",end="")
                else:
                    for k in range(n):
                        if k==0 or k==n-1:
                           print("*",end="")
                        else:
                            print(" ",end="")
                print()
                        
                
              
sol=Solution()
n=2
sol.pattern21(n)