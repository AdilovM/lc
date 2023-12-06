# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        path_sum = 0
        stack = [root]
        while stack:
            current_node = stack.pop()
            if current_node:
                if low <= current_node.val <= high:
                    path_sum += current_node.val
                if current_node.val > low:
                    stack.append(current_node.left)
                if current_node.val < high:
                    stack.append(current_node.right)
        return path_sum
                    