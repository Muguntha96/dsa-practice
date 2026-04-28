# Given a binary tree, return true if it is height-balanced and false otherwise.

# A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example 1:

# Input: root = [1,2,3,null,null,4]

# Output: true

from typing import Optional
from tree_utils import TreeNode, build_tree

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True
            left=dfs(root.left)
            if left==-1:
                return -1
            right=dfs(root.right)
            if right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return dfs(root)!=-1

root=build_tree([1,2,3,None,None,4])
sol=Solution()
print(sol.isBalanced(root))