from collections import Counter
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        m = Counter(arr)
        ans = 0
        arr.sort()
        for i in range(len(arr) - 1):
            if m[arr[i]] and m[arr[i] + 1]:
                ans += 1
        return ans
