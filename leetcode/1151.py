from collections import Counter
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ans = 10 ** 5
        l = ones = zeros = 0
        n = len(data)
        m = Counter(data)
        if m[1] == 0:
            return 0
        for i in range(n):
            if data[i]:
                ones += 1
            else:
                zeros += 1
            if ones + zeros == m[1]:
                ans = min(ans, zeros)
                if data[l]:
                    ones -= 1
                else:
                    zeros -= 1
                l += 1
        return ans
