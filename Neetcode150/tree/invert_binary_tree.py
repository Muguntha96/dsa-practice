# You are given the root of a binary tree root. Invert the binary tree and return its root.

# Example 1:

# Input: root = [1,2,3,4,5,6,7]

# Output: [1,3,2,7,6,5,4]



from typing import Optional
from tree_utils import TreeNode, build_tree, print_tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp=root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

root = build_tree([1,2,3,4,5,6,7])

sol = Solution()

print("Original:")
print_tree(root)

sol.invertTree(root)

print("Inverted:")
print_tree(root)