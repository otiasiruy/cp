from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(curr, sum, id):
            if sum == target:
                ans.append(curr[:])
                return
            elif sum > target:
                return
            for i in range(id, n):
                curr.append(candidates[i])
                backtrack(curr, sum + candidates[i], id)
                id += 1
                curr.pop()

        candidates.sort()
        n = len(candidates)
        ans = []
        backtrack([], 0, 0)
        return ans