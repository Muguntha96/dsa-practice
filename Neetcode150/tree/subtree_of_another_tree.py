# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example 1:

# Input: root = [1,2,3,4,5], subRoot = [2,4,5]

# Output: true

# Example 2:

# Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

# Output: false

# Constraints:

#     1 <= The number of nodes in both trees <= 100.
#     -100 <= root.val, subRoot.val <= 100


from typing import Optional
from tree_utils import TreeNode, build_tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        return False

root = build_tree([1,2,3,4,5])
subRoot = build_tree([2,4,5])
sol = Solution()
print(sol.isSubtree(root, subRoot))