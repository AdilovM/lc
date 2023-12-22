# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # init defaultdict to store column : [nodes]
        col_table = defaultdict(list)
        
        # populate defaultdict by BFS
        q = deque([(root, 0)])
        
        while q:
            node, col = q.popleft()
            if node:
                col_table[col].append(node.val)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        
        # sort nodes based on column
        return [val for key, val in sorted(col_table.items())]
        
        # return result