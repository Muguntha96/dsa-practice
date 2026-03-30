# # print_recursion/sum_of_n_ntural_numbers.py
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15
class Solution:
    def sumofN(self, n: int,sum:int) -> int:
        if n == 0:
            return 0
        return self.sumofN(n-1,sum+n)
        
        

        

sol=Solution()
n=5

print(sol.sumofN(n,0))