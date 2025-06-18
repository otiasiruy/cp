from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        g = []
        for i in range(1, len(nums) + 1):
            g.append(nums[i - 1])
            if i % 3 == 0:
                if g[2] - g[0] > k:
                    return []
                ans.append(g)
                g = []
        return ans