# 143. Reorder List
# Solved
# Medium
# Topics
# premium lock iconCompanies

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

# Example 1:

# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
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
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        list1=head
        list2=slow.next
        slow.next=None
        prev=None
        cur=list2
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        list2=prev
        while list2:
            temp1=list1.next
            temp2=list2.next

            list1.next=list2
            list2.next=temp1

            list1=temp1
            list2=temp2


if __name__ == "__main__":
    # Create list [1,2,3,4] with a cycle connecting tail to index 1
    head = build_linked_list([1,2,3,4])

    sol = Solution()
    sol.reorderList(head)
    print_list(head)
  