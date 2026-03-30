# Factorial of a Number : Iterative and Recursive

# Problem Statement: Given a number X,  print its factorial.

# To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

# Note: X  is always a positive number. 
class Solution:
    def factofN(self,n:int,fact:int)->int:
        if n==0:
            return fact
        return self.factofN(n-1,fact*n)
sol=Solution()
n=5
print(sol.factofN(n,1))