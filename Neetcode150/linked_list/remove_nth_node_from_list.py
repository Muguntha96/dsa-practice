# Remove Node From End of Linked List
# Medium Topics Company Tags
# Hints

# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4]

# Example 2:

# Input: head = [5], n = 1

# Output: []
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first=second=head
        for _ in range(n):
            first=first.next
        if first is None:
            return head.next
        while first.next:
            first=first.next
            second=second.next
        second.next=second.next.next
        return head
nums = [1,2,3,4]
n=2
head = build_linked_list(nums)     

sol = Solution()
remove_nthnode = sol.removeNthFromEnd(head,n)   

print_linked_list(remove_nthnode)       