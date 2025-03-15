from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        n = rows * cols
        ans = []
        r = c = 0
        count = 0
        up = left = 0
        while count < n:

            for i in range(left, cols):
                ans.append(matrix[up][i])
                count += 1
                if count == n:
                    return ans

            for i in range(up + 1, rows):
                ans.append(matrix[i][cols - 1])
                count += 1
                if count == n:
                    return ans

            for i in range(cols - 2, left - 1, -1):
                ans.append(matrix[rows - 1][i])
                count += 1
                if count == n:
                    return ans

            for i in range(rows - 2, up, -1):
                ans.append(matrix[i][left])
                count += 1
                if count == n:
                    return ans

            cols -= 1
            rows -= 1
            left += 1
            up += 1
            print(f"count {count}")

        return ans