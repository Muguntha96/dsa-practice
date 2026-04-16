# Given an integer n, for every positive integer i <= n, the task is to print,

#     "FizzBuzz" if i is divisible by 3 and 5,
#     "Fizz" if i is divisible by 3,
#     "Buzz" if i is divisible by 5
#     "i" as a string, if none of the conditions are true.

from typing import List


class Solution:
    def fizzbuzz(self,n:int)->List:
        fizzbuzz={
            3:'fizz',
            5:'buzz'
        }
        divisors=[3,5]
        res=[]
        for i in range(1,n+1):
            word=""
            for d in divisors:
                if i%d==0:
                    word+=fizzbuzz[d]
            if word:
                res.append(word)
            else:
                res.append(i)
                
        return res
sol=Solution()
n=5
print(sol.fizzbuzz(n))    
