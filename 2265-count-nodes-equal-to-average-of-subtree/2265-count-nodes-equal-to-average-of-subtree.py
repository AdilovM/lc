# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0
            
            left_sum, left_count, left_res = dfs(node.left)
            right_sum, right_count, right_res = dfs(node.right)
            
            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1
            
            # Calculate average and round down as it's usually done in integer division
            if subtree_sum // subtree_count == node.val:
                return subtree_sum, subtree_count, left_res + right_res + 1
            else:
                return subtree_sum, subtree_count, left_res + right_res

        _, _, result = dfs(root)
        return result