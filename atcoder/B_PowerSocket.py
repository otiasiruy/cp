import bisect
import os
import sys
from collections import Counter, deque
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():

    a, b = list(map(int, input().split()))
    if b == 1:
        print(0)
        return
    s = 1
    sm = a
    while sm < b:
        sm += a - 1
        s += 1
    print(s)


if __name__ == "__main__":
    solve()