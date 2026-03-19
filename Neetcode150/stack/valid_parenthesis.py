# Easy Topics Company Tags
# Hints

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
from typing import List
class Solution:
    def validParenthesis(self,s:str)->bool:
        stack=[]
        mapping={'}':'{',')':'(',']':'['}

        for c in s:
            if c in mapping:
                if stack and stack[-1]==mapping[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
sol=Solution()

s = "[]"
print(sol.validParenthesis(s))