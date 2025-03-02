from collections import defaultdict
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        for i in range(len(nums) - k + 1):
            s = set()
            for j in range(i, k + i):
                if nums[j] not in s:
                    m[nums[j]] += 1
                    s.add(nums[j])
        ans = -1
        for k, v in m.items():
            if v == 1:
                ans = max(ans, k)
        return ans