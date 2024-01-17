# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal and store the values
        def inOrderTraversal(node):
            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right) if node else []
        
        # Helper function to construct a balanced BST from sorted array
        def sortedArrayToBST(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])
            return root

        # Convert the BST to a sorted array
        sorted_vals = inOrderTraversal(root)

        # Construct a balanced BST from the sorted array
        return sortedArrayToBST(sorted_vals)