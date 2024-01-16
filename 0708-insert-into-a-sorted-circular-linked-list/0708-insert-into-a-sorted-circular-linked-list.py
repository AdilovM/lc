"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        
        # If the list is empty, create a new single-node circle and return.
        if not head:
            new_node.next = new_node
            return new_node
        
        # If the list is not empty.
        current = head
        while True:
            # Case 1: Insert between two nodes.
            if current.val <= insertVal <= current.next.val:
                break
            
            # Case 2: At the end or beginning of the list (where the list wraps around).
            # This is for handling the case where insertVal is greater than any element in the list
            # or smaller than any element in the list.
            if current.val > current.next.val:
                if insertVal >= current.val or insertVal <= current.next.val:
                    break

            # Move to the next node.
            current = current.next
            
            # If we have gone through one full loop, insert the node next to head.
            if current == head:
                break
        
        # Insert the new node.
        new_node.next = current.next
        current.next = new_node
        
        return head