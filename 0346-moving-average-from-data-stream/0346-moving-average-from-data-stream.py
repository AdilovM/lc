class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = []

    def next(self, val: int) -> float:
        size, q = self.size, self.q
        q.append(val)
        window = sum(q[-size:])
        return window / min(len(q), size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)