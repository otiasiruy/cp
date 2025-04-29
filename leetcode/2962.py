from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        cnt = 0
        w = 0
        lmx = []
        for i in range(len(nums)):
            if nums[i] == mx:
                w += 1
                lmx.append(i)
            if w >= k:
                cnt += 1
                if len(lmx) >= k:
                    cnt += lmx[len(lmx) - k]
        return cnt