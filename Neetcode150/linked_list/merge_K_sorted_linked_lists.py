# Merge K Sorted Linked Lists
# Hard Topics Company Tags
# Hints

# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.

# Example 1:

# Input: lists = [[1,2,4],[1,3,5],[3,6]]

# Output: [1,1,2,3,3,4,5,6]

# Example 2:

# Input: lists = []

# Output: []

# Example 3:

# Input: lists = [[]]

# Output: []

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists)==0:
            return None
        while len(lists)>1:
            mergedLists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                mergedLists.append(self.merge2Lists(l1,l2))
            lists=mergedLists
        return lists[0]
        

    def merge2Lists(self,l1,l2):
        dummy=ListNode()
        tail=dummy
        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next
                tail=tail.next
            else:
                tail.next=l2
                l2=l2.next
                tail=tail.next
        tail.next=l1 or l2
        return dummy.next

def build_list(arr):
    dummy = ListNode()
    cur = dummy

    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")   

lists_input = [[1,2,4],[1,3,5],[3,6]]

lists = [build_list(arr) for arr in lists_input]

sol = Solution()
result = sol.mergeKLists(lists)

print_list(result)