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
        x = list(map(int, input().split()))
        c = Counter(x)
        for k, v in c.items():
            if v == 1:
                for i in range(len(x)):
                    if x[i] == k:
                        print(i + 1)
                        break

if __name__ == "__main__":
    solve()