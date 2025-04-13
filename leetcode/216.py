from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtracking(arr, id):
            if sum(arr) > n or len(arr) > k:
                return
            if sum(arr) == n and len(arr) == k:
                ans.append(arr[:])
                return
            for i in range(id, 10):
                if i not in arr:
                    arr.append(i)
                    backtracking(arr, i + 1)
                    arr.pop()

        ans = []
        backtracking([], 1)
        return ans