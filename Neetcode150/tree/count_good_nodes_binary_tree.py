# Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

# Given the root of a binary tree root, return the number of good nodes within the tree.

# Example 1:

# Input: root = [2,1,1,3,null,1,5]

# Output: 3
from typing import Optional,List
from tree_utils import TreeNode, build_tree
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxVal):
            if not node:
                return 0
            res = 1 if node.val>=maxVal else 0
            maxVal=max(node.val,maxVal)
            res +=dfs(node.left,maxVal)
            res +=dfs(node.right,maxVal)
            return res
        return dfs(root,root.val)

root=build_tree([2,1,1,3,None,1,5])
sol=Solution()
print(sol.goodNodes(root))

