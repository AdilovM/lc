class ListNode(object):
  def __init__(self, val=0, next = None):
    self.val = val
    self.next = next

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    new_node = ListNode(value)
    if self.head is None or self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
      return self

ll1 = LinkedList()
ll1.append(1)
ll1.append(1)
ll1.append(1)
ll1.append(2)
ll1.append(2)
ll1.append(3)

# current_node = ll1.head
# while current_node:
#   print(current_node.val)
#   current_node = current_node.next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        current = head
        nxt = head.next
        while nxt:
            if current.val == nxt.val:
                current.next = nxt.next
                nxt = current
                print(f'nxt.val = {nxt.val}')
            current = nxt
            print(f'current.val = {current.val}')
            nxt = nxt.next
            if nxt is not None:
              print(f'nxt.val = {nxt.val}')
        return head

solution = Solution()
solution.deleteDuplicates(ll1.head)




# current_node = ll1.head
# while current_node:
#   print(current_node.val)
#   current_node = current_node.next