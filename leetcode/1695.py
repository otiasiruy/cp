from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        psum = 0
        l = 0
        s = set()
        n = len(nums)
        for i in range(n):
            psum += nums[i]
            if nums[i] not in s:
                ans = max(ans, psum)
            else:
                while nums[i] in s:
                    psum -= nums[l]
                    s.remove(nums[l])
                    l += 1
            s.add(nums[i]) 
        return ans