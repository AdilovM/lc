# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        found_null = False

        while queue:
            node = queue.popleft()

            if not node:
                found_null = True
            else:
                if found_null:
                    # Found a non-null node after a null node, so the tree is not complete
                    return False
                queue.append(node.left)
                queue.append(node.right)

        # If no non-null nodes are found after a null node, the tree is complete
        return True