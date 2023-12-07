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
            t1, t2 = stack.pop()
            # add t1 and t2 values
            t1.val += t2.val
            
            # if t1 left and t2 left exist, add them
            if t1.left and t2.left:
                stack.append((t1.left, t2.left))
            # if no t1 left, t2 left becomes t1 left
            elif not t1.left:
                t1.left = t2.left
            
            # if t1 right and t2 right exist, add them
            if t1.right and t2.right:
                stack.append((t1.right, t2.right))
            # if no t1 right, t2 right becomes t1 right
            elif not t1.right:
                t1.right = t2.right
                
        return root1