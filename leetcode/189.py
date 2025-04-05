from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = nums.copy()
        for i in range(n):
            id = (i + k) % n
            nums[id] = tmp[i]