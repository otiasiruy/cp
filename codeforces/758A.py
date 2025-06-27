import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    t = int(input())
    x = list(map(int, input().split()))
    cnt = 0
    mx = max(x)
    while t > 0:
        t -= 1
        cnt += mx - x[t]
    print(cnt)


if __name__ == "__main__":
    solve()