from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        s = set()
        for i in range(n - 2):
            v1 = nums[i]
            l = i + 1
            r = n - 1
            if i == 0 or nums[i - 1] != nums[i]:
                while l < r:
                    if v1 + nums[l] + nums[r] == 0 and (v1, nums[l], nums[r]) not in s:
                        ans.append([v1, nums[l], nums[r]])
                        s.add((v1, nums[l], nums[r]))
                        continue
                    elif (v1, nums[l], nums[r]) in s:
                        l += 1
                    elif v1 + nums[l] + nums[r] < 0:
                        l += 1
                    elif v1 + nums[l] + nums[r] > 0:
                        r -= 1
        return ans