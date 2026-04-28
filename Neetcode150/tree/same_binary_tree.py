# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]

# Output: true
from typing import Optional
from tree_utils import TreeNode, build_tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False

p=build_tree([1,2,4])    
q=build_tree([1,2,3])
sol=Solution()
print(sol.isSameTree(p,q))

