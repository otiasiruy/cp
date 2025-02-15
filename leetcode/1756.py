from collections import deque


class MRUQueue:
    dq = deque()

    def __init__(self, n: int):
        MRUQueue.dq = deque()
        for i in range(1, n + 1):
            MRUQueue.dq.append(i)

    def fetch(self, k: int) -> int:
        tmp = MRUQueue.dq[k - 1]
        del MRUQueue.dq[k - 1]
        MRUQueue.dq.append(tmp)
        return tmp
