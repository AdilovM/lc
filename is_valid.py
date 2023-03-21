from typing import List
class Solution(object):
  def is_valid(self, str):
    Map = {
      ']' : '[',
      ')' : '(',
      '}' : '{'
    }
    stack = []
    for char in str:
      if char not in Map:
        stack.append(char)
      elif not stack or stack[-1] != Map[char]:
        return False
      else:
        stack.pop()
    return not stack

solution = Solution()
print(solution.is_valid('([{}])()'))