from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            cp = ''.join(sorted(w))
            if cp not in d:
                d[cp] = [w]
            else:
                d[cp].append(w)
        ans = []
        for k, v in d.items():
            l = []
            for i in v:
                l.append(i)
            ans.append(l)
        return ans