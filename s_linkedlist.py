class Node:
  def __init__(self,value, next = None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def prepend(self, value):
    new_node = Node(value, next = self.head)
    self.head = new_node
    if self.tail is None:
      self.tail = new_node

  def append(self, value):
    new_node = Node(value)
    if self.head is None or self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    return self


ll_1 = LinkedList()
ll_1.prepend(3)
ll_1.prepend(2)
ll_1.prepend(1)
# ll_1.append(4)
# ll_1.append(5)
# ll_1.append(6)

print(ll_1.tail.value)