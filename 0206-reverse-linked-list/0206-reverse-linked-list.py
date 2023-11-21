# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            # save the next node
            temp = curr.next
            # next become prev
            curr.next = prev
            # prev becomes curr
            prev = curr
            # curr become original curr.next (temp)
            curr = temp
            # move the next node
        # return prev. after exiting the loop prev is the last node in original ll
        return prev