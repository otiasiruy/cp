import os
import sys
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    def bs(v):
        l = 0
        r = len(x) - 1
        while l < r:
            md = l + (r - l)//2
            if x[md] > v:
                r = md
            else:
                l = md + 1
        return l

    n = int(input())
    x = sorted(list(map(int, input().split())))
    t = q = int(input())
    while t > 0:
        t -= 1
        m = int(input())
        i = bs(m)
        if i == 0 and x[i] <= m:
            print(1)
        elif i > 0:
            print(i+1 if x[i] <= m else i)
        else:
            print(0)



if __name__ == "__main__":
    solve()