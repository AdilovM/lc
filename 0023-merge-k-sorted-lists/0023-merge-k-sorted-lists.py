# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a dummy node and initialize the current node
        dummy = ListNode(None)
        curr = dummy

        # Custom comparison function for ListNode
        ListNode.__lt__ = lambda self, other: self.val < other.val

        # Initialize a priority queue
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(l)

        # Iterate over the priority queue until it's empty
        while not q.empty():
            # Get the smallest node and append it to the merged list
            node = q.get()
            curr.next = node
            curr = curr.next

            # If there is a next node, put it into the queue
            if node.next:
                q.put(node.next)

        return dummy.next
                
            