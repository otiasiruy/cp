from collections import defaultdict
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = defaultdict(list)
        for c in votes[0]:
            for i in range(len(votes[0])):
                d[c].append(1000)
        for v in votes:
            length = len(v)
            for c in v:
                id = v.find(c)
                d[c][id] -= 1
        l = []
        for k, v in d.items():
            v.append(k)
            l.append(tuple(v))
        ranked = sorted(l)
        ans = []
        for t in ranked:
            ans.append(t[len(t) - 1])
        return ''.join(ans)