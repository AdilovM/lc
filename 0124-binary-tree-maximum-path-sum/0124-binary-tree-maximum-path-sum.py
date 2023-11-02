# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        1. using helper dfs return max value between (left child max sum and right child max sum) + parent node value
        2. max sum value is max value between what helper dfs returns and zero bc if child's max sum is negative we should not add it to global max sum value
        3. global max is max between current global max and sum of children values and current node value
        4. assign nonlocal variable answer that represents final answer
        5. if given node is null then return 0
        """
        
        global_max_sum = float('-inf')
        
        def helper_dfs(node):
            nonlocal global_max_sum
            if not node:
                return 0
            
            left_path_max_sum = max(helper_dfs(node.left), 0)
            right_path_max_sum = max(helper_dfs(node.right), 0)
            
            global_max_sum = max(global_max_sum,left_path_max_sum + right_path_max_sum + node.val)
            
            return max(left_path_max_sum, right_path_max_sum) + node.val
        
        helper_dfs(root)
        return global_max_sum