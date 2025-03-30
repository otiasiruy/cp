from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        l = []
        d = defaultdict(int)
        while node:
            l.append(node.val)
            d[node.val] += 1
            node = node.next
        head = None
        prev = None
        for v in l:
            if not head and d[v] == 1:
                head = ListNode(v, None)
                prev = head
            elif head and d[v] == 1:
                node = ListNode(v, None)
                prev.next = node
                prev = node
        return head
