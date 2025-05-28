from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        w = 1
        v = nums[0]
        for i in range(1, n):
            if nums[i] == v and w < 2:
                nums[k] = nums[i]
                w += 1
                k += 1
            elif nums[i] == v and w == 2:
                continue
            elif nums[i] != v:
                nums[k] = nums[i]
                k += 1
                v = nums[i]
                w = 1
        return k