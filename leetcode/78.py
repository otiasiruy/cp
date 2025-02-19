from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(id, sub):

            ans.append(sub[:])

            for i in range(id, len(nums)):
                sub.append(nums[i])
                backtrack(i + 1, sub)
                sub.pop()

        ans = []
        backtrack(0, [])
        return ans