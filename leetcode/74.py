from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(x, arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = l + (r - l)//2
                if arr[m] == x:
                    return m
                elif arr[m] < x:
                    l = m + 1
                else:
                    r = m - 1
            return l - 1
        r = [row[0] for row in matrix]
        i = bs(target, r)
        if matrix[i][0] == target:
            return True
        j = bs(target, matrix[i])
        if matrix[i][j] == target:
            return True
        return False