# Kth Smallest Integer in BST
# Medium Topics Company Tags
# Hints

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

# A binary search tree satisfies the following constraints:

#     The left subtree of every node contains only nodes with keys less than the node's key.
#     The right subtree of every node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees are also binary search trees.

# Example 1:

# Input: root = [2,1,3], k = 1

# Output: 1
from typing import Optional

from tree_utils import TreeNode,build_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        cur=root
        stack=[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            n+=1
            if n==k:
                return cur.val
            cur=cur.right

root=build_tree([2,1,3])
k=1
sol=Solution()
print(sol.kthSmallest(root,k))
