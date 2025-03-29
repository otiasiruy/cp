from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        dq = deque()
        while head:
            dq.append(head.val)
            head = head.next
        n = len(dq)
        for i in range(n):
            ans += pow(2, i) * dq.pop()
        return ans