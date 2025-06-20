import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n = int(input())
    cnt = 0
    x = [100, 20, 10, 5, 1]
    i = 0
    while n % x[i] != 0:
        if x[i] <= n:
            cnt += n // x[i]
            n = n % x[i]
#        print(f"n {n}, i {i}, x[i] {x[i]}, n % x[i] {n % x[i]}, cnt {cnt}")
        i += 1
    cnt += n // x[i]
    print(cnt)

if __name__ == "__main__":
    solve()