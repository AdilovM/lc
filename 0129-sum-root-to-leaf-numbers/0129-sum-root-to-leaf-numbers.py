# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_number):
            if not node:
                return 0

            current_number = current_number * 10 + node.val
            
            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return current_number

            # Recursively call for left and right children
            return dfs(node.left, current_number) + dfs(node.right, current_number)

        return dfs(root, 0)
        
            
        