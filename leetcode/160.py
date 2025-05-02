from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        nodeA = headA
        while nodeA:
            seen.add(nodeA)
            nodeA = nodeA.next
        nodeB = headB
        while nodeB:
            if nodeB in seen:
                return nodeB
            nodeB = nodeB.next
        return None