from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def bs(x):
            l = 0
            r = len(intervals) - 1
            while l <= r:
                m = l + (r - l)//2
                if st[m][0] == x:
                    return m
                elif st[m][0] < x:
                    l = m + 1
                else:
                    r = m - 1
            return l

        st = []
        end = []
        seq = 0
        for i, j in intervals:
            st.append((i, seq))
            end.append((j, seq))
            seq += 1
        st.sort()
        end.sort()
        ans = []
        for i in range(len(end)):
            id = bs(intervals[i][1])
            #print(f"intervals[i][1] {intervals[i][1]}, id {id}")
            if 0 <= id < len(end):
                if st[id][0] >= intervals[i][1]:
                    ans.append(st[id][1])
                else:
                    ans.append(-1)
            else:
                ans.append(-1)
        return ans