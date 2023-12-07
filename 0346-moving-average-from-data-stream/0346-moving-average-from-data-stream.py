class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.vals = []
    def next(self, val: int) -> float:
        size, vals = self.size, self.vals
        vals.append(val)
        window = sum(vals[-size:])
        return window  / min(len(vals), size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)