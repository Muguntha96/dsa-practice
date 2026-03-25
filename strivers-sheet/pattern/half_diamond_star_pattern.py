# Input Format: N = 6
# Result:   
#      *
#      **
#      *** 
#      ****
#      *****
#      ******  
#      *****
#      ****
#      ***    
#      **
#      *
class Solution:
    def pattern10(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*",end="")
            print()
        for i in range(n-1,0,-1):
            for j in range(i):
                print("*",end="")
            print()




sol=Solution()
n=3
sol.pattern10(n)