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
        a, b, c = list(map(int, input().split()))
        if a + b == c:
            print('+')
        else:
            print('-')

if __name__ == "__main__":
    solve()