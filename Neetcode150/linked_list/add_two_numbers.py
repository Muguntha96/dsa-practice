# Add Two Numbers
# Medium Topics Company Tags
# Hints

# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Example 1:

# Input: l1 = [1,2,3], l2 = [4,5,6]

# Output: [5,7,9]

# Explanation: 321 + 654 = 975.
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
    return res

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dummy=ListNode()
        curr=dummy
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            total=val1+val2+carry
            carry=total//10
            digit=total%10
            curr.next=ListNode(digit)
            curr=curr.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next
        



if __name__ == "__main__":
    l1=build_linked_list([1,2,3])
    l2=build_linked_list([4,5,6])

    sol = Solution()
    add_two_numbers=sol.addTwoNumbers(l1,l2)
    print(print_linked_list(add_two_numbers))