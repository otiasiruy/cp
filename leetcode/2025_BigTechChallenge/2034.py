from bisect import bisect


class StockPrice:

    def __init__(self):
        self.prices = []
        self.index = {}
        self.curr_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        new = (price, timestamp)
        if timestamp in self.index:
            old = self.index[timestamp]
            self.prices.remove(old)
        bisect.insort(self.prices, new)
        self.index[timestamp] = new
        self.curr_timestamp = max(self.curr_timestamp, timestamp)

    def current(self) -> int:
        return self.index[self.curr_timestamp][0]

    def maximum(self) -> int:
        return self.prices[len(self.prices) - 1][0]

    def minimum(self) -> int:
        return self.prices[0][0]

