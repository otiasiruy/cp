from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if slow and slow.next:
            slow.next = slow.next.next
        return head