# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = float('-inf')
        def helper_dfs(node):
            nonlocal answer
            if not node:
                return 0
            
            max_left_path = max(helper_dfs(node.left), 0)
            max_right_path = max(helper_dfs(node.right), 0)
            
            answer = max(answer, max_left_path + max_right_path + node.val)
            
            return max(max_left_path, max_right_path) + node.val
        
        helper_dfs(root)
        return answer