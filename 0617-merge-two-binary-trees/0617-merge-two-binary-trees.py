# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        stack = [(root1, root2)]
        while stack:
            t1_current_node, t2_current_node = stack.pop()

            # Add the values from both nodes
            t1_current_node.val += t2_current_node.val

            # Handle left child
            if t1_current_node.left and t2_current_node.left:
                stack.append((t1_current_node.left, t2_current_node.left))
            elif not t1_current_node.left:
                t1_current_node.left = t2_current_node.left

            # Handle right child
            if t1_current_node.right and t2_current_node.right:
                stack.append((t1_current_node.right, t2_current_node.right))
            elif not t1_current_node.right:
                t1_current_node.right = t2_current_node.right

        return root1
            