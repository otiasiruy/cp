class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = 0
        n = len(nums)
        l = 0
        w = 1
        for i in range(n):
            w *= nums[i]
            while w >= k:
                w /= nums[l]
                l += 1
            ans += i - l + 1
        return ans