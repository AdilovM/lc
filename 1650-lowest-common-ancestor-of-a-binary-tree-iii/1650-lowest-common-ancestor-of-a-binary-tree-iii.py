"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
       # Create two pointers starting at nodes p and q
        a, b = p, q

        # Iterate until both pointers meet at the LCA
        while a != b:
            # If a reaches root (None), restart it at q
            a = a.parent if a else q
            # If b reaches root (None), restart it at p
            b = b.parent if b else p

        # At this point, a and b point to the LCA
        return a
