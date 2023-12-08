# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # dict of lists
        column_table = defaultdict(list)
        # create q and add (root, 0) as first element
        q = deque([(root, 0)])
        # while element in q
        while q:
            # pop (node, column)
            node, column = q.popleft()
            # if node exists add node.val at column_table[column]
            if node:
                column_table[column].append(node.val)
                # append node.left to left side from root
                q.append((node.left, column - 1))
                q.append((node.right, column + 1))
        return [column_table[x] for x in sorted(column_table.keys())]