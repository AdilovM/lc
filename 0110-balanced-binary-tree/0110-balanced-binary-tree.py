# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0
            l_height = get_height(node.left)
            r_height = get_height(node.right)
            if abs(l_height - r_height) > 1 or l_height == -1 or r_height == -1:
                return -1
            return 1 + max(l_height, r_height)
        
        return get_height(root) != -1
    
        