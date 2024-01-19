# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # Helper function to perform DFS and return the depth and node
        def dfs(node):
            if not node:
                return 0, None
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            # If left and right depths are equal, current node is LCA
            if left_depth == right_depth:
                return left_depth + 1, node
            # If left is deeper, return left node, otherwise right node
            return (left_depth + 1, left_node) if left_depth > right_depth else (right_depth + 1, right_node)

        # Call DFS and return the node part of the tuple
        return dfs(root)[1]