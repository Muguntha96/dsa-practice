# print n to 1
# n=5 (5,4,3,2,1)
class Solution:
    def printNto1(self,n:int):
        if n==0:
            return
        print(n)
        self.printNto1(n-1)
        

sol=Solution()
n=5
print(sol.printNto1(n))