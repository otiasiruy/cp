from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_el = arr[n - 1]
        max_l = [0] * n
        for i in range(n - 2, -1, -1):
            max_el = max(max_el, arr[i + 1])
            max_l[i] = max_el
        for i in range(n):
            if i == n - 1:
                arr[i] = -1
                return arr
            arr[i] = max_l[i]