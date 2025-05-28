import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        cnt = 0
        d = defaultdict(int)
        for i in range(n):
            cnt += d[a[i] - i]
            d[a[i] - i] += 1
        print(cnt)


if __name__ == "__main__":
    solve()