import bisect
import os
import sys
from collections import Counter, deque
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():

    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    v = a[0]
    mx = 0
    for i in range(1, n):
        if v > a[i]:
            mx = max(mx, i - l)
            l = i
        v = a[i]
    mx = max(mx, n - l)
    print(mx)


if __name__ == "__main__":
    solve()