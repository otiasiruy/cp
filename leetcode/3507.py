from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def non_decreasing(arr):
            n = len(arr)
            if n == 1:
                return True
            for i in range(1, n):
                if arr[i - 1] > arr[i]:
                    return False
            return True
        ans = 0
        dq = nums[:]
        total = len(nums)
        id = -2
        while not non_decreasing(dq):
            min_sum = 10**9
            n = len(dq)
            id = -1
            for i in range(1, n):
                p_sum = dq[i - 1] + dq[i]
                if min_sum > p_sum:
                    min_sum = p_sum
                    id = i
            tmp_dq = []
            for i in range(n):
                if i + 1 == id:
                    tmp_dq.append(min_sum)
                elif i == id:
                    continue
                else:
                    tmp_dq.append(dq[i])
            ans += 1
            dq = tmp_dq[:]
        return ans