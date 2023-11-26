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
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
                return -1
            return 1 + max(left_height, right_height)
        
        return get_height(root) != -1