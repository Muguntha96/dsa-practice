# Given the root of a binary tree, return its depth.

# The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# Input: root = [1,2,3,null,null,4]

# Output: 3
from typing import Optional
from tree_utils import TreeNode, build_tree, print_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

root = build_tree([1,2,3,None,None,4])

sol = Solution()



print(sol.maxDepth(root))


