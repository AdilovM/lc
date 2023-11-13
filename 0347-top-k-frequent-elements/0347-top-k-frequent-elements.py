from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1.map number to its count
        2.bucket (list of lists) where index for num is num's count and inner list consits of nums mapped to that count
        3.traverse the bucket backwards to return the K most freq elements
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        frequency_list = [(number, freq) for number, freq in counts.items()]
        
        frequency_list.sort(key=lambda x: x[1], reverse=True)
  
        top_k = [number for number, freq in frequency_list[:k]]

        return top_k