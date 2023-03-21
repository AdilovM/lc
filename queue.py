class Node(object):
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

class Queue(object):
  def __init__(self):
    self.front = None
    self.back = None

  def enqueue(self, val):
    new_node = Node(val)
    if self.front is None or self.back is None:
      self.front = new_node
      self.back = new_node
    else:
      self.back.next = new_node
      self.back = new_node

  def dequeue(self):
    if self.front is None:
      return
    else:
      current_front = self.front
      self.front = self.front.next
      return current_front


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue().val)
print(q.dequeue().val)
print(q.dequeue().val)
print(q.dequeue())