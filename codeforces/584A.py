import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n, t = list(map(int, input().split()))
    if t == 10:
        if n < 2:
            print(-1)
        else:
            print(10**(n-1))
    else:
        print(t*10**(n-1))


if __name__ == "__main__":
    solve()