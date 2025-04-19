from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        ps = 0
        pl = 0
        l = 0
        for i in range(n):
            pl += 1
            ps += nums[i]
            if pl * ps < k:
                ans += pl
            while pl * ps >= k:
                pl -= 1
                ps -= nums[l]
                l += 1
                if pl * ps < k:
                    ans += pl
        return ans
