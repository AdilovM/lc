class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        output = [intervals[0]]
        
        for currStart, currEnd in intervals[1:]:
            lastEnd = output[-1][1]
            if currStart <= lastEnd:
                output[-1][1] = max(currEnd, lastEnd)
            else:
                output.append([currStart, currEnd])
        return output
            