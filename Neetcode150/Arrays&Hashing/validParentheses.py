# 20. Valid Parentheses
# Easy
# Topics
# premium lock iconCompanies
# Hint

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false
# Answer:
from typing import List
class Solution:
    def validParentheses(self,s:str)->bool:
        seen=set()
        for i in range(len(s)):
            if s[i] in seen:
                return True
            seen.add(s[i])
        return False
sol=Solution()
s= "()[]{}"
print(sol.validParentheses(s))