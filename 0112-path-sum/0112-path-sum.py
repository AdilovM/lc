# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        recursively subtract current root.val from targetSum and if no more children left return if root.val equals to current targetSum.
        if there are more children return next recursive call on left child or right child, either of them can return False or True
        """
        # base case 1
        if not root:
            return False
        # if no more children left
        if not root.left and not root.right:
            return root.val == targetSum
        
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)