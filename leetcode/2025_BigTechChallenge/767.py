import heapq
from collections import defaultdict


class Solution:

    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] -= 1
        l = []
        for k, v in d.items():
            heapq.heappush(l, (v, k))
        ans = []
        pre = ''
        while len(l) > 0:
            v, k = heapq.heappop(l)
            if pre == k:
                return ""
            ans.append(k)
            pre = k
            if len(l) > 0:
                v2, k2 = heapq.heappop(l)
                if pre == k2:
                    return ""
                ans.append(k2)
                pre = k2
                if v2 < -1:
                    v2 += 1
                    heapq.heappush(l, (v2, k2))
            if v < -1:
                v += 1
                heapq.heappush(l, (v, k))

        return ''.join(ans)