from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sum_digits(x):
            s = str(x)
            total = 0
            for c in s:
                total += int(c)
            return total

        c = defaultdict(int)
        for i in range(1, n + 1):
            c[sum_digits(i)] += 1
        largest_gp = max(c.values())
        ans = 0
        for k, v in c.items():
            if v == largest_gp:
                ans += 1
        return ans