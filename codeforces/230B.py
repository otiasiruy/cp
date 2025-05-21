import os
import sys
from math import sqrt

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    lim = 1000001
    prime = [True] * lim
    prime[0] = prime[1] = False
    i = 2
    while i*i < lim:
        if prime[i]:
            for j in range(i*i, lim, i):
                prime[j] = False
        i += 1

    for i in x:
        q = int(sqrt(i))
        print("YES" if q*q == i and prime[q] else "NO")

if __name__ == "__main__":
    solve()