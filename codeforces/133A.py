import bisect
import os
import sys
from collections import Counter, deque
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():

    p = input()
    d = {'H', 'Q', '9'}
    for c in p:
        if c in d:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    solve()