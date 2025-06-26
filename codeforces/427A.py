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
    sm = 0
    i = 0
    while t > 0:
        t -= 1
        sm = sm + x[i]
        if sm < 0 and x[i] < 0:
            cnt += 1
            sm = 0
        i += 1
    print(cnt)


if __name__ == "__main__":
    solve()