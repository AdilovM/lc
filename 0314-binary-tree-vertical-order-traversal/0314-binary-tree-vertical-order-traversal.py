# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # dictionary to hold the vertical order traversal
        vertical = defaultdict(list)
        # queue for level order traversal, with node and its horizontal distance
        queue = deque([(root, 0)])

        while queue:
            node, hd = queue.popleft()

            # append the current node to its respective vertical level
            vertical[hd].append(node.val)

            # enqueue left child with horizontal distance hd-1
            if node.left:
                queue.append((node.left, hd - 1))

            # enqueue right child with horizontal distance hd+1
            if node.right:
                queue.append((node.right, hd + 1))

        # extract the values from the dictionary in sorted order of keys
        return [vertical[key] for key in sorted(vertical)]