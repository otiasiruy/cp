import os
import sys
from collections import Counter
from math import ceil

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

#def list_ints():
#    return list(map(int, input().split()))

def solve():

    n = int(input())
    gp = list(map(int, input().split()))
    c = Counter(gp)
    cnt = 0
    for i in range(4, 0, -1):
        if i == 4:
            cnt += c[4]
        elif i == 3:
            cnt += c[3]
            c[1] = max(0, c[1] - c[3])
        elif i == 2:
            if c[2] % 2 == 0:
                cnt += c[2] // 2
            elif c[2] == 1:
                cnt += 1
                if c[1] > 0:
                    c[1] = max(0, c[1] - 2)
            else:
                cnt += (c[2] - 1) // 2 + 1
                if c[1] > 0:
                    c[1] = max(0, c[1] - 2)
        else:
            cnt += int(ceil(c[1]/4))
    print(cnt)

if __name__ == "__main__":
    solve()