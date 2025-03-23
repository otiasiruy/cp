from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        a, b = toBeRemoved[0], toBeRemoved[1]
        for i in intervals:
            if i[1] <= a:
                ans.append(i)
            elif i[0] < a and i[1] > a and i[1] <= b:
                ans.append([i[0], a])
            elif i[0] < a and i[1] > a and i[1] > b:
                ans.append([i[0], a])
                ans.append([b, i[1]])
            elif i[0] >= b:
                ans.append(i)
            elif i[0] < b and i[1] > b:
                ans.append([b, i[1]])
        return ans