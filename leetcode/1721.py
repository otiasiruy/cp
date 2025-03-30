from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        node = sentinel
        index = 0
        total = 0
        prev1 = sentinel
        node1 = head
        prev2 = sentinel
        node2 = head
        while node:
            if index == k - 1:
                prev1 = node
                node1 = node.next
            index += 1
            node = node.next
            total += 1

        k2 = total - k
        index2 = 0
        node = sentinel

        while node:
            if index2 == k2 - 1:
                prev2 = node
                node2 = node.next
                break
            index2 += 1
            node = node.next

        prev1.next = node2
        tmp = None
        prev2.next = node1
        tmp = node2.next
        node2.next = node1.next
        node1.next = tmp
        return sentinel.next