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
        x, y = list(map(int, input().split()))
        a, b = list(map(int, input().split()))
        c = 0
        mx = max(x, y)
        mi = min(x, y)
        if 2 * a > b:
            c = mi * b
            c += abs(x - y) * a
            print(c)
        else:
            print((x+y)*a)


if __name__ == "__main__":
    solve()