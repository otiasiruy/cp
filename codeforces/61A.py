import os
import sys
from collections import Counter, defaultdict
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    x = input()
    y = input()
    ans = []
    for i in range(len(x)):
        if x[i] == y[i]:
            ans.append('0')
        else:
            ans.append('1')
    print(''.join(ans))

if __name__ == "__main__":
    solve()