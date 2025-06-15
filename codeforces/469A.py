import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    s = set(x[1:])
    s.update(y[1:])
    for i in range(1, n + 1):
        if i not in s:
            print("Oh, my keyboard!")
            return
    print("I become the guy.")

if __name__ == "__main__":
    solve()