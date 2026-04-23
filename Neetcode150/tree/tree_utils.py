from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level_list):
    if not level_list:
        return None

    root = TreeNode(level_list[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_list):
        node = queue.popleft()

        if level_list[i] is not None:
            node.left = TreeNode(level_list[i])
            queue.append(node.left)
        i += 1

        if i < len(level_list) and level_list[i] is not None:
            node.right = TreeNode(level_list[i])
            queue.append(node.right)
        i += 1

    return root


def print_tree(root):
    if not root:
        print([])
        return

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)

            queue.append(node.left)
            queue.append(node.right)

    print(result)