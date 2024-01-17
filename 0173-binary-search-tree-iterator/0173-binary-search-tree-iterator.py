# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._leftmost_inorder(root)
    
    def _leftmost_inorder(self, root):
        # Push all nodes along the path to the leftmost node onto the stack
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # Pop the top node (next smallest element)
        top_node = self.stack.pop()

        # If the node has a right child, process its leftmost subtree
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        
        return top_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()