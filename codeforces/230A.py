import os
import sys
from collections import Counter
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    s, n = list(map(int, input().split()))
    b = []
    while n > 0:
        n -= 1
        x, y = list(map(int, input().split()))
        b.append((x, y))
    b.sort()
    for x, y in b:
        if s > x:
            s += y
        else:
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    solve()