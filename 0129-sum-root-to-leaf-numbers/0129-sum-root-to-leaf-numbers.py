# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = curr_number = 0

        while root:
            # Check if the current node has a left child
            if root.left:
                # Finding the inorder predecessor of the current node
                predecessor = root.left
                steps = 1  # To count the number of steps to revert the current number later
                # Finding the rightmost child of the left subtree or the already visited node
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Establish a temporary link from the predecessor to the current node
                if predecessor.right is None:
                    curr_number = curr_number * 10 + root.val  # Update the current number
                    predecessor.right = root  # Make the temporary link
                    root = root.left  # Move to the left child
                else:
                    # If there is a temporary link, it means we have visited the left subtree
                    # Check if it's a leaf node to update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # Reverting the current number to its parent node's number
                    for _ in range(steps):
                        curr_number //= 10
                    # Remove the temporary link and move to the right subtree
                    predecessor.right = None
                    root = root.right
            else:
                # Update the current number and move to the right child
                curr_number = curr_number * 10 + root.val
                # Check if it's a leaf node to update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf
        
            
        