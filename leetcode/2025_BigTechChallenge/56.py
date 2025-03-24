from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        a = intervals[0][0]
        b = intervals[0][1]
        for i in intervals:
            if a < i[0] and b < i[0]:
                ans.append([a, b])
                a = i[0]
                b = i[1]
            elif a <= i[0] <= b <= i[1]:
                b = i[1]
            elif i[0] < a < i[1] and b < i[1]:
                a = i[0]
                b = i[1]
        ans.append([a, b])
        return ans