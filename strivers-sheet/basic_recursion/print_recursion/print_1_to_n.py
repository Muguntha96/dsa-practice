# print 1-n using recursion
# eg n=4,(1,2,3,4)
class Solution:
    def printN(self,n:int,i:int):
        if i>n:
            return
        else:
            print(i)
        self.printN(n,i+1)

sol=Solution()
n=5
i=1
print(sol.printN(n,i))