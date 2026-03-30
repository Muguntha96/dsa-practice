# bactracking
class Solution:
    def printNbacktracking(self,n:int):
        
        if n<=0:
            return
        self.printNbacktracking(n-1)
        print(n)
    def printNto1Backtracking(self,i:int,n:int):        
        if i>n:
            return
        self.printNto1Backtracking(i+1,n)
        print(i)
sol=Solution()
n=5
print("1 to n backtracking")
print(sol.printNbacktracking(n))
i=1
print("n to 1 backtracking")
print(sol.printNto1Backtracking(i,n))