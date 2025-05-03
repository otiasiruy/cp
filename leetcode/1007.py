from collections import Counter
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t = Counter(tops)
        b = Counter(bottoms)
        l = [1,2,3,4,5,6]
        n = len(tops)
        mtv = 0
        mtn = 0
        for k, v in t.items():
            if mtv < v:
                mtv = v
                mtn = k
        cnt = 0
        anst = 0
        for i in range(n):
            if tops[i] == mtn:
                cnt += 1
            elif bottoms[i] == mtn:
                cnt += 1
                anst += 1
        if cnt != n:
            anst = n + 1

        mbv = 0
        mbn = 0
        for k, v in b.items():
            if mbv < v:
                mbv = v
                mbn = k
        cnt = 0
        ansb = 0
        for i in range(n):
            if bottoms[i] == mbn:
                cnt += 1
            elif tops[i] == mbn:
                cnt += 1
                ansb += 1
        if cnt != n:
            ansb = n + 1
        ans = min(anst, ansb)
        return -1 if ans == n + 1 else ans