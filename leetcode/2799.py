from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c = Counter(nums)
        length = len(c)
        cw = Counter()
        ans = 0
        l = 0
        r = 0
        for i in nums:
            r += 1
            cw[i] += 1
            while len(cw) == length:
                ans += len(nums) - r + 1
                v = nums[l]
                if cw[v] == 1:
                    del cw[v]
                else:
                    cw[v] -= 1
                l += 1
        return ans