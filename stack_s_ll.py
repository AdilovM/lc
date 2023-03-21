class Node(object):
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Stack(object):
  def __init__(self):
    self.top = None
    self.count = 0

  def push(self, val):
    new_node = Node(val, self.top)
    self.top = new_node
    self.count += 1

  def pop(self):
    current_top = self.top
    self.top = self.top.next
    self.count -= 1
    return current_top

# stack = Stack()
# stack.push(5)
# stack.push(4)
# stack.push(7)
# print(stack.pop().val)
# print(stack.pop().val)
# print(stack.count)