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

    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(' '.join(map(str, a)))




if __name__ == "__main__":
    solve()