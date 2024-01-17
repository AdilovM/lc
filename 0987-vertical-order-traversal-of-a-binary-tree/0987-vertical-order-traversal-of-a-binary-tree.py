# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_list = []

        # DFS function to traverse the tree and record node positions
        def dfs(node, row, col):
            if node:
                node_list.append((col, row, node.val))
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        # Start DFS with the root node at position (row=0, col=0)
        dfs(root, 0, 0)

        # Sort the node list
        node_list.sort()

        # Group the nodes by their column and extract the values
        result = []
        current_column_index = node_list[0][0]
        current_column = []

        for col, row, val in node_list:
            if col == current_column_index:
                current_column.append(val)
            else:
                result.append(current_column)
                current_column_index = col
                current_column = [val]

        result.append(current_column)
        return result