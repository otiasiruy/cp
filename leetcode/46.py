from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(subseq):
            if len(subseq) == n:
                ans.append(subseq[:])
                return

            for i in range(n):
                if nums[i] not in subseq:
                    subseq.append(nums[i])
                    backtrack(subseq)
                    subseq.pop()

        n = len(nums)
        subseq = []
        ans = []
        backtrack(subseq)

        return ans