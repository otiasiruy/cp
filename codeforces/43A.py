import os
import sys
from collections import Counter
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n = int(input())
    g = []
    while  n > 0:
        n -= 1
        g.append(input())
    c = Counter(g)
    ans, mx = "", 0
    for k, v in c.items():
        if mx < v:
            mx = v
            ans = k
    print(ans)


if __name__ == "__main__":
    solve()