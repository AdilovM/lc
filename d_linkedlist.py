class Node(object):
  def __init__(self, val, prev = None, next = None):
    self.val = val
    self.prev = prev
    self.next = next

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def prepend(self, val):
    new_node = Node(val)
    if self.head is None:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

    if self.tail is None:
      self.tail = new_node

  def append(self, val):
    new_node = Node(val)
    if self.head is None or self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    return self

  def print_nodes(self):
    if self.head is None:
      return None
    else:
      current_node = self.head
      while current_node:
        print(current_node.val)
        current_node = current_node.next

  def remove_node(self, val):
    if self.head.val == val:
      self.head = self.head.next
      return
    else:
      current_node = self.head
      while current_node.next:
        if current_node.next.val == val:
          current_node.next = current_node.next.next
        else:
          current_node = current_node.next
      return

ll_1 = LinkedList()
ll_1.prepend(3)
ll_1.prepend(2)
ll_1.prepend(1)
ll_1.append(4)
ll_1.append(5)
ll_1.append(6)
# ll_1.print_nodes()
ll_1.remove_node(4)
ll_1.print_nodes()
# print(ll_1.head.next.val)
