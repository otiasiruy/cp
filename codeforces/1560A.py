import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    t = int(input())
    tt = t
    x = []
    mx = 0
    while tt > 0:
        tt -= 1
        x.append(int(input()))
        mx = max(mx, x[-1])
    seq = []
    i = 1
    while len(seq) < mx:
        if i % 3 != 0 and str(i)[-1] != '3':
            seq.append(i)
        i += 1
    i = 0
    while t > 0:
        t -= 1
        print(seq[x[i] - 1])
        i += 1

if __name__ == "__main__":
    solve()