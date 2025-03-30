from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_odd = None
        head_even = None
        node_odd = None
        node_even = None
        node = head
        index = 0
        while node:
            index += 1
            if index % 2 != 0:
                if not head_odd:
                    head_odd = node
                    node_odd = node
                else:
                    node_odd.next = node
                    node_odd = node

            else:
                if not head_even:
                    head_even = node
                    node_even = node
                else:
                    node_even.next = node
                    node_even = node

            node = node.next

        if node_even:
            node_even.next = None
        if node_odd:
            node_odd.next = head_even

        return head_odd