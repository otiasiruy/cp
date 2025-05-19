import os
import sys

if os.path.exists('input'):
    sys.stdin = open('input', 'r')
    sys.stdout = open('output', 'w')

def solve():

    a, b = list(map(int, input().split()))
    if b == 1:
        print(0)
        return
    s = 1
    sm = a
    while sm < b:
        sm += a - 1
        s += 1
    print(s)


if __name__ == "__main__":
    solve()