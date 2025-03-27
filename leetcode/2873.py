from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ml, mr = [0] * n, [0] * n
        ml[0] = nums[0]
        mr[n - 1] = nums[n - 1]
        for i in range(1, n):
            ml[i] = max(ml[i - 1], nums[i])
            mr[n - 1 - i] = max(mr[n - i], nums[n - 1 - i])
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, (ml[i - 1] - nums[i]) * mr[i + 1])
        return ans