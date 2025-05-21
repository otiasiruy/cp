import os
import sys
from collections import defaultdict

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n, m, a, b = list(map(int, input().split()))
    if b < a * m:
        ct = (n // m) * b
    else:
        ct = n * a
    r = n % m
    ex = 0
    if r != 0:
        ex = min(r * a, b)
    print(ct + ex)

if __name__ == "__main__":
    solve()