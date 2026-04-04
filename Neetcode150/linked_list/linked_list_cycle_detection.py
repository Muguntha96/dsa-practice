# Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

# There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

# Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

# # Note: index is not given to you as a parameter.

# # Example 1:

# Input: head = [1,2,3,4], index = 1

# Output: tru
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Build linked list and optionally create a cycle
def build_linked_list(arr, cycle_index: int = -1):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    nodes = [head]  # Keep track of nodes to create cycle
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
    # Create cycle if cycle_index is valid
    if 0 <= cycle_index < len(nodes):
        curr.next = nodes[cycle_index]
    return head

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    # Create list [1,2,3,4] with a cycle connecting tail to index 1
    head = build_linked_list([1,2,3,4], cycle_index=1)

    sol = Solution()
    detect_cycle = sol.hasCycle(head)
    print(detect_cycle)  