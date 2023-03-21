def is_increasing(nums):
  if len(nums) == 2 and nums[0] < nums[1]:
    return True
  elif nums[0] < nums[1]:
    return is_increasing(nums[1:])
  else:
    return False
print(is_increasing([1,0,3,4]))