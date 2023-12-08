class Solution:
    def frequencySort(self, s: str) -> str:
        # count chars in s
        counts = collections.Counter(s)
        # get max freq for buckets size
        max_freq = max(counts.values())
        # create a bucket. start index 1
        buckets = [[] for _ in range(max_freq + 1)]
        # fill the fucket
        for c, i in counts.items():
            buckets[i].append(c)
            
        # going from R to L build the string
        str_builder = []
        
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                str_builder.append(c * i)
        return "".join(str_builder)