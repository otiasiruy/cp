from collections import defaultdict


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s = set()
        d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        mp = defaultdict()
        mp['N'] = 0
        mp['S']= 1
        mp['E'] = 2
        mp['W'] = 3
        x = y = 0
        s.add((x,y))
        for p in path:
            x += d[mp[p]][0]
            y += d[mp[p]][1]
            if (x,y) in s:
                return True
            s.add((x,y))
        return False