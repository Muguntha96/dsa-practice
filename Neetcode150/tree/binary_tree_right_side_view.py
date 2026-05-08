# You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

# Example 1:

# Input: root = [1,2,3,null,4,null,5]

# Output: [1,3,5]
import collections
from typing import Optional,List
from tree_utils import TreeNode, build_tree
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque([root])
        while q:
            rightSide=None
            qLen=len(q)
            for i in range(qLen):
                node=q.popleft()
                if node:
                    rightSide=node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

root=build_tree([1,2,3,None,4,None,5])
sol=Solution()
print(sol.rightSideView(root))