# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.
from collections import deque


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        dq = deque()
        dq.append(head)
        while head:
            head = head.getNext()
            dq.append(head)
        while dq:
            node = dq.pop()
            if node:
                node.printValue()
