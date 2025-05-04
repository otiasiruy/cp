from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def bs(arr, x):
            n = len(arr)
            l, r = 0, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] < x:
                    l = mid + 1
                elif arr[mid] > x:
                    r = mid - 1
                else:
                    return mid + 1
            return l
        n = len(nums)
        nums.sort()
        ps = [0] * n
        ps[0] = nums[0]
        for i in range(1, n):
            ps[i] += ps[i - 1] + nums[i]
        ans = []
        for i in queries:
            ans.append(bs(ps, i))
        return ans