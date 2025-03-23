class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return pow(n, 2) if pow(n, 2) * w <= maxWeight else maxWeight // w