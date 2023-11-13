from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1.map number to its count
        2.bucket (list of lists) where index for num is num's count and inner list consits of nums mapped to that count
        3.traverse the bucket backwards to return the K most freq elements
        """
        # counts = {}
        # bucket = [[] for _ in range(len(nums) + 1)]
        
        # for num in nums:
        #     counts[num] = 1 + counts.get(num, 0)
        # c = Coun
        # res = counts.most_common()
        # return res[:k+1]
        
        counts = Counter(nums)
        res = []
        for n,f in counts.most_common():
            res.append(n)
            if len(res) == k:
                return res
        
            
            
            
#         for num, count in counts.items():
#             bucket[count].append(num)

#         res = []
#         for idx in range(len(bucket) - 1, 0, -1):
#             for n in bucket[idx]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res

  
