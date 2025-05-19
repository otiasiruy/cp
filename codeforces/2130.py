from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dq = deque()
        while head:
            dq.append(head.val)
            head = head.next
        n = len(dq)
        l = 0
        r = n - 1
        mx = 0
        while l < r:
            mx = max(mx, dq[l] + dq[r])
            l += 1
            r -= 1
        return mx