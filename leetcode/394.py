from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque(s)
        ans = deque()
        while stack:
            c = stack.pop()
            if c == '[':
                num = deque()
                c = stack.pop()
                num.append(c)
                while stack and c.isnumeric():
                    c = stack.pop()
                    if c.isnumeric():
                        num.appendleft(c)
                    else:
                        stack.append(c)
                x = int(''.join(num))
                l = []
                c = ans.popleft()
                while c != ']':
                    l.append(c)
                    c = ans.popleft()
                for _ in range(x):
                    ans.appendleft(''.join(l))
            else:
                ans.appendleft(c)
        return ''.join(ans)