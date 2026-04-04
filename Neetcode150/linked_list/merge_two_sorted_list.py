# Merge Two Sorted Linked Lists
# Easy Topics Company Tags
# Hints

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to build linked list from Python list
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print(res)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        node=dummy
        while list1 and list2:
            if list1.val<list2.val:
                node.next=list1
                list1=list1.next
            else:
                node.next=list2
                list2=list2.next
            node=node.next
        node.next=list1 or list2
        return dummy.next

if __name__ == "__main__":
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])

    sol = Solution()
    merged_head = sol.mergeTwoLists(list1, list2)

    print_linked_list(merged_head)