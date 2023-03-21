class Binary_Tree_Node:
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right

  def add_node(self, data):
    if data == self.data:
      return
    if data < self.data:
      if self.left:
        self.left.add_node(data)
      else:
        self.left = Binary_Tree_Node(data)
    else:
      if self.right:
        self.right.add_node(data)
      else:
        self.right = Binary_Tree_Node(data)

  def find_node(self,data):
    if self.data is None:
      return False
    if data == self.data:
      return True
    if data < self.data:
      if self.left:
        return self.left.find_node(data)
      else:
        return False
    if data > self.data:
      if self.right:
        return self.right.find_node(data)
      else:
        return False






bst = Binary_Tree_Node(6)
bst.add_node(6)
bst.add_node(5)
bst.add_node(7)

# print(bst.data, bst.left.data, bst.right.data)
print(bst.find_node(5))
