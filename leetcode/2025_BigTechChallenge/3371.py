from collections import Counter
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        s = Counter(nums)
        ans = -1001
        for i in range(n):
            sub_total = total - nums[i]
            if sub_total % 2 == 1:
                continue
            k = sub_total / 2
            if k in s and (nums[i] != k or s[nums[i]] > 1):
                ans = max(ans, nums[i])
        return ans