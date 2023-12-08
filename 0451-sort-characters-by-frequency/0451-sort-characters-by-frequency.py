class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        str_builder = []
        for l, f in counts.most_common():
            str_builder.append(l * f)
        return "".join(str_builder)