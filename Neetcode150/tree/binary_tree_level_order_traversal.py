# Binary Tree Level Order Traversal
# Medium Topics Company Tags
# Hints

# Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Example 1:

# Input: root = [1,2,3,4,5,6,7]

# Output: [[1],[2,3],[4,5,6,7]]

# Example 2:

# Input: root = [1]

# Output: [[1]]
import collections
from typing import Optional,List
from tree_utils import TreeNode, build_tree
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            qLen=len(q)
            level=[]
            for i in range(qLen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

root=build_tree([1,2,3,4,5,6,7])
sol=Solution()
print(sol.levelOrder(root))