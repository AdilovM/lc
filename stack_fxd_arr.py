class Stack():
  def __init__(self,max_size):
    self.items = []
    self.max_size = max_size

  def top(self):
    if len(self.items) > 0:
      return self.items[-1]
    else:
      print('empty stack')

  def pop(self):
    if len(self.items) > 0:
      temp = self.top()
      del self.items[-1]
      return temp
    else:
      print('empty stack')

  def is_empty(self):
    return True if len(self.items) == 0 else False

  def push(self, value):
    print('overflow') if len(self.items) == self.max_size else self.items.append(value)







s1 = Stack(5)
print(s1.pop())
s1.push(9)
s1.push(6)
print(s1.items)
s1.push(100)
print(s1.items)
print(s1.is_empty())
print(s1.top())
s1.pop()
print(s1.items)
s1.push(8)
s1.push(-1)
s1.push(0)
s1.push(-55)
s1.push(-56)
print(s1.items)
