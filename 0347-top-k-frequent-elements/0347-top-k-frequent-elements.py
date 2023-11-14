class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        freq_list = [(num, freq) for num, freq in counts.items()]
        freq_list.sort(key=lambda x:x[1], reverse=True)
        top_k = [num for num, freq in freq_list[:k]]
        return top_k