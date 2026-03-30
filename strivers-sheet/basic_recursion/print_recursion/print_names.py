# print names 5 times
class Solution:
    def printName(self,n:int,i:int):
        if i>n:
            return
        print("Muguntha")
        self.printName(n,i+1)
        
        
sol=Solution()
n=5
i=1
print(sol.printName(n,i))