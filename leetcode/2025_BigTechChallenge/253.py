from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        n = len(intervals)

        for l in intervals:
            start.append(l[0])
            end.append(l[1])

        start = sorted(start)
        end = sorted(end)

        ans = 0
        endId = 0
        i = 0

        while i < n:
            if start[i] >= end[endId]:
                ans -= 1
                endId += 1
            ans += 1
            i += 1

        return ans