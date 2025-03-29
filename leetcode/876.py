from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        node = head
        while node:
            node = node.next
            c += 1
        c //= 2
        while c > 0:
            head = head.next
            c -= 1
        return head