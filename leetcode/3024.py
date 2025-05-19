from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        c = {}
        for i in range(len(nums)):
            if nums[i - 1] + nums[i] <= nums[(i + 1) % len(nums)]:
                return "none"
            c[nums[i]] = 1
        if len(c) == 1:
            return "equilateral"
        elif len(c) == 2:
            return "isosceles"
        return "scalene"