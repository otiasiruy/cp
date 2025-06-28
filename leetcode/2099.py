from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l = nums.copy()
        l.sort()
        l = l[len(l) - k:]
        ans = []
        for i in nums:
            if i in l:
                ans.append(i)
                l.remove(i)
        return ans