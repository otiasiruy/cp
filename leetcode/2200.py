from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        id = []
        seen = set()
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                id.append(j)
        for i in range(n):
            for j in id:
                if abs(i - j) <= k and i not in seen:
                    ans.append(i)
                    seen.add(i)
        ans.sort()
        return ans