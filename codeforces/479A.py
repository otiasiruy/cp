import bisect
import sys
from collections import deque
import os
from math import gcd

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

#def list_ints():
#    return list(map(int, input().split()))

def solve():

    a = int(input())
    b = int(input())
    c = int(input())
    mx = 0
    if a == 1:
        mx = a + b
        if c == 1:
            mx += c
        else:
            mx *= c
    elif b == 1:
        if a < c:
            mx = (a + b) * c
        elif a > c:
            mx = (c + b) * a
        elif a == c and a > 1:
            mx = (a + b) * c
        else:
            mx = a + b + c
    elif c == 1:
        mx = b + c
        if a == 1:
            mx += a
        else:
            mx *= a
    else:
        mx = a * b * c
    print(mx)



if __name__ == "__main__":
    solve()