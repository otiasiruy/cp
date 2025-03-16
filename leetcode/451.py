from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        ans = []
        l = []
        for k, v in c.items():
            l.append((v, k))
        l.sort(reverse=True)
        for v, k in l:
            for i in range(v):
                ans.append(k)
        return ''.join(ans)