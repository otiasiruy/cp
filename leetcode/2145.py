from typing import List


class Solution:
    def numberOfArrays(self, diff: List[int], l: int, u: int) -> int:
        n = len(diff)
        arr = [0] * (n + 1)
        j = 0
        arr[0] = l
        up = False
        ds = 0
        di = 0
        ms = 10**6
        mi = 10**6
        ms = min(ms, u - arr[j])
        mi = min(mi, arr[j] - l)
        for i in diff:
            arr[j + 1] = i + arr[j]
            ms = min(ms, u - arr[j + 1])
            mi = min(mi, arr[j + 1] - l)
            if arr[j + 1] > u:
                ds = max(ds, abs(arr[j + 1] - u))
            if arr[j + 1] < l:
                di = max(di, abs(arr[j + 1] - l))
            j += 1
        if ds > 0 and di > 0:
            return 0
        elif di > 0:
            return ms - di + 1 if ms - di + 1 > 0 else 0
        elif ds > 0:
            return mi - ds + 1 if mi - ds + 1 > 0 else 0
        else:
            return mi + ms + 1