from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i, j, k = 0, 0, 0
        n = len(nums)
        ans = 0
        max_l, max_r = [0] * n, [0] * n
        max_l[0] = nums[0]
        max_r[n - 1] = nums[n - 1]
        for i in range(1, n):
            max_l[i] = max(max_l[i - 1], nums[i])
            max_r[n - 1 - i] = max(max_r[n - i], nums[n -1 - i])

        for i in range(1, n - 1):
            ans = max(ans, (max_l[i - 1] - nums[i]) * max_r[i + 1])
        return ans
