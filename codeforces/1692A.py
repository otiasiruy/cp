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
        x = list(map(int, input().split()))
        a = x[0]
        cnt = 0
        for i in range(1, 4):
            if x[i] > a:
                cnt += 1
        print(cnt)

if __name__ == "__main__":
    solve()