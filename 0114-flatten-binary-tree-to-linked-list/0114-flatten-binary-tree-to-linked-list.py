# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # Flatten left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)

        # If there is a left subtree, we need to rewire
        if root.left:
            # Find the rightmost node in the left subtree
            rightmost = root.left
            while rightmost.right:
                rightmost = rightmost.right

            # Rewire the right subtree to the rightmost node
            rightmost.right = root.right

            # Move the left subtree to the right
            root.right = root.left
            root.left = None