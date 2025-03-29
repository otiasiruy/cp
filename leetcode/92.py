from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l_node, r_node = None, None
        node = head
        l = []
        il = []
        i = 1
        while node:
            if i == left:
                while i != right:
                    il.append(node.val)
                    node = node.next
                    i += 1
                il.append(node.val)
                il.reverse()
                l += il
                node = node.next
            else:
                l.append(node.val)
                node = node.next
            i += 1
        n = len(l)
        head = ListNode(l[0], None)
        prev = head
        for i in range(1, n):
            node = ListNode(l[i], None)
            prev.next = node
            prev = node
        return head