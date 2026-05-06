# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.

# Example 1:

# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

# Output: 5

# Example 2:

# Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

# Output: 3

# Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.
from typing import Optional
from tree_utils import TreeNode, build_tree
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr=root
        while curr:
            if p.val<curr.val and q.val<curr.val:
                curr=curr.left
            elif p.val>curr.val and q.val>curr.val:
                curr=curr.right
            else:
                return curr

root=build_tree([5,3,8,1,4,7,9,None,2])
p=TreeNode(3)
q=TreeNode(8)
sol=Solution()
result=sol.lowestCommonAncestor(root,p,q)
print(result.val)