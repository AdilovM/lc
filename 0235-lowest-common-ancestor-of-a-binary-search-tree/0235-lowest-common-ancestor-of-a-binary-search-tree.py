# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        # Recursively find LCA in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # Recursively find LCA in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-null, current node is the LCA
        if left and right:
            return root

        # Otherwise, return the non-null value among left and right, 
        # which indicates where a target node was found, or return None if neither was found
        return left if left else right