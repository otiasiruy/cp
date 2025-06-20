import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    r, c = list(map(int, input().split()))
    ed = True
    for i in range(r):
        for j in range(c):
            if i % 2 == 0:
                print("#", end="")
            else:
                if ed and j == c - 1:
                    print("#", end="")
                elif not ed and j == 0:
                    print("#", end="")
                else:
                    print(".", end="")
        if i % 2 != 0:
            ed = not ed
        if i != r - 1:
            print()

if __name__ == "__main__":
    solve()