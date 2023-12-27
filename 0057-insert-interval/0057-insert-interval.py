class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # newinterval gets prepended
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # intervals[i] is less than newinterval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # newinterval overlaps with current interval. newInterval is min(newinterval[0],i[0]) and max(newinterval[0], i[0])
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        # newInterval gets appended
        res.append(newInterval)
        return res
                
            
            
                
            