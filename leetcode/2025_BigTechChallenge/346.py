from collections import deque


class MovingAverage:
    dq = deque()
    size = 0
    s = 0.0
    def __init__(self, size: int):
        self.size = size
        self.dq = deque()
        self.s = 0.0

    def next(self, val: int) -> float:
        if len(self.dq) < self.size:
            self.dq.append(val)
            self.s += val
        else:
            v = self.dq.popleft()
            self.s -= v
            self.dq.append(val)
            self.s += val
        return self.s / float (len(self.dq))
