import re
class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if not s.isalpha():
      s = re.sub('[!@#$%^&*()[]{};:,./<>?\|`~-=_+]', '' ,s).replace(' ','').lower()
      print(s)
    if len(s) <= 1:
      return True
    if len(s) >=2 and s[0].lower() != s[-1].lower():
      return False

    if len(s) > 1 and s[0].lower() == s[-1].lower():
      return self.isPalindrome(s[1:-1])


solution = Solution()

print(solution.isPalindrome("A man, a plan, a canal: Panama"))