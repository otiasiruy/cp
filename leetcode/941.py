from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        c1 = True
        peak_found = False
        if arr[0] >= arr[1]:
            return False
        for i in range(2, n):
            if arr[i - 1] == arr[i]:
                return False
            elif arr[i - 1] > arr[i] and not peak_found:
                peak_found = True
            elif arr[i - 1] < arr[i] and peak_found:
                return False
        return True if peak_found else False