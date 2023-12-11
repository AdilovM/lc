"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        head = None
        prev = None

        def inorder(node):
            nonlocal head, prev
            if not node:
                return

            # In-order traversal: Left -> Node -> Right
            inorder(node.left)

            if prev:
                # Link the previous node (smaller) with the current one
                node.left = prev
                prev.right = node
            else:
                # Initialize head for the first node
                head = node

            # Update the previous node
            prev = node

            inorder(node.right)

        inorder(root)

        # Close the circular list
        if head and prev:
            head.left = prev
            prev.right = head

        return head