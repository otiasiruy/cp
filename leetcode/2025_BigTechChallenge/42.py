from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lm = 0
        rm = 0
        ans = 0
        while l <= r:
            if height[l] >= height[r]:
                rm = max(rm, height[r])
                ans += rm - height[r]
                r -= 1
            else:
                lm = max(lm, height[l])
                ans += lm - height[l]
                l += 1
        return ans