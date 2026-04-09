# Copy Linked List with Random Pointer
# Medium Topics Company Tags
# Hints

# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

#     The original value val of the copied node
#     A next pointer to the new node corresponding to the next pointer of the original node
#     A random pointer to the new node corresponding to the random pointer of the original node

# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:

# Input: head = [[3,null],[7,3],[4,0],[5,1]]

class Node:
    def __init__(self,val=0,next=None,random=None):
        self.val=val
        self.next=next
        self.random=random
def build_linked_list(arr):
    if not arr:
        return None
    head=Node(arr[0][0])
    curr=head
    nodes=[Node(val) for val,_ in arr]
    for i in range(len(nodes)-1):
        nodes[i].next=nodes[i+1]
    for i, (_, rand_index) in enumerate(arr):
        if rand_index is not None:
            nodes[i].random = nodes[rand_index]

    return nodes[0]


def print_linked_list(head):
    res = []
    curr = head

    while curr:
        random_val = curr.random.val if curr.random else None
        res.append([curr.val, random_val])
        curr = curr.next

    return res

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map={}
        curr=head
        while curr:
            copy=Node(curr.val)
            copy.next=None
            copy.random=None
            map[curr]=copy
            curr=curr.next
        curr=head
        while curr:
            copy=map[curr]
            copy.next=map.get(curr.next)
            copy.random=map.get(curr.random)
            curr=curr.next
        copied_head=map[head]
        return copied_head
arr=[[3,None],[7,3],[4,0],[5,1]]
head=build_linked_list(arr)
print("original")
print(print_linked_list(head))
sol=Solution()
print("copied")
copied_list=sol.copyRandomList(head)
print(print_linked_list(copied_list))