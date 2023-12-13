# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_table = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, column = q.popleft()
            if node:
                column_table[column].append(node.val)
                q.append((node.left, column - 1))
                q.append((node.right, column + 1))
        
        column_table = sorted(column_table.items())
        
        output = []
        for idx, lst in column_table:
            output.append(lst)
        
        return output
        