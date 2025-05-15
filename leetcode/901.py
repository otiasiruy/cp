class StockSpanner:

    def __init__(self):
        self.ms = []
        self.id = -1

    def next(self, price: int) -> int:
        i = self.id
        while self.ms and self.ms[i][1] <= price:
            steps, p = self.ms[i]
            i = max(-1, i - steps)
            if i == -1:
                break
        self.id += 1
        self.ms.append((self.id - i, price))
        return self.id - i