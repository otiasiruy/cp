import os
import sys
from collections import defaultdict

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n = int(input())
    d = defaultdict(int)
    while n > 0:
        n -= 1
        nm = input()
        if nm not in d:
            d[nm] = 1
            print("OK")
        else:
            new_nm = nm + str(d[nm])
            d[nm] += 1
            print(new_nm)
            d[new_nm] = 1


if __name__ == "__main__":
    solve()