# You are given the head of a singly linked list head and a positive integer k.

# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

# Return the modified list after reversing the nodes in each group of k.

# You are only allowed to modify the nodes' next pointers, not the values of the nodes.

# Example 1:

# Input: head = [1,2,3,4,5,6], k = 3

# Output: [3,2,1,6,5,4]
from typing import Optional

# Node definition
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        groupPrev=dummy
        while True:
            kth=self.getKth(groupPrev,k)
            if kth is None:
                break
            groupNext=kth.next
            prev=groupNext
            curr=groupPrev.next
            while curr!=groupNext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=groupPrev.next
            groupPrev.next=kth
            groupPrev=temp

        return dummy.next


    def getKth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr

nums = [1,2,3,4,5,6]
k=3
head = build_linked_list(nums)     

sol = Solution()
new_head = sol.reverseKGroup(head,k) 
print_linked_list(new_head)