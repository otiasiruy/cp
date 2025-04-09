class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        m = x
        while l <= r:
            m = (l + r) // 2
            q = m * m
            if q == x or (q < x and (m + 1) * (m + 1) > x):
                return m
            elif q < x:
                l = m + 1
            else:
                r = m - 1
        return m