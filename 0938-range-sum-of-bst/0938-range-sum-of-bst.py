# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node, path_sum):
            if node:
                if low <= node.val <= high:
                    path_sum += node.val

                if node.val > low:
                    path_sum = dfs(node.left, path_sum)
                if node.val < high:
                    path_sum = dfs(node.right, path_sum)

            return path_sum
        
        return dfs(root, 0)
            