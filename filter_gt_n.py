def filter_gt_n(lst, n):
  if not lst:
    return []
  else:
    if lst[0] > n:
      print([lst[0]])
      return [lst[0]] + filter_gt_n(lst[1:], n)
    else:
      return filter_gt_n(lst[1:], n)

print(filter_gt_n([4,3,4, 9, 10, 11,5,6,2,0], 5))
# print(filter_gt_n([], 5))
# print([1,2,34] + [2,4])
# def filter_gt_n(lst, n):
# # your code here
#   sorted(lst)
#   if len(lst)<1:
#     print ([])
#   elif lst[0]>n:
#     return (lst)
#   elif lst[-1]<=n:
#     print ([])
#   else:
#     return filter_gt_n(lst[1:],n)
#   return
