import heapq
from typing import List, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        c = Counter(tasks)
        l = []
        for k, v in c.items():
            heapq.heappush(l, (v * (-1), k))
        while l:
            count = -1
            length = len(l)
            tmp = []
            for i in range(length):
                count += 1
                ans += 1
                v, k = heapq.heappop(l)
                if v < -1:
                    v += 1
                    tmp.append((v, k))
                if count == n:
                    break
            if tmp:
                for v, k in tmp:
                    heapq.heappush(l, (v, k))
            if count < n and l:
                ans += n - count
        return ans