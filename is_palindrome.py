def is_palindrome(x):
  # find how many digits
  if x == 0:
    return True
  if x < 0:
    return False

  def rec(nums):
    if len(nums) == 1:
        return True
    elif len(nums) == 2 and nums[0] == nums[1]:
        return True
    elif nums[0] == nums[-1]:
        return rec(nums[1:-1])
    elif nums[0] != nums[-1]:
        return False
    else:
        return False

  separate_digits = []
  while x >= 1:
    separate_digits.append(x % 10)
    x = int(x/10)
  return rec(separate_digits)

print(is_palindrome(11211))



