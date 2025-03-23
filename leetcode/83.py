from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if not node:
                return

            if node.next and node.val == node.next.val:
                node.next = node.next.next
                helper(node)
            elif node.next:
                helper(node.next)

        helper(head)
        return head