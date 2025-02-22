from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        m = []
        g = []
        for i in nums:
            if i < pivot:
                l.append(i)
            elif i > pivot:
                g.append(i)
            else:
                m.append(i)
        return l + m + g