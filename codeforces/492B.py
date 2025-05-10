import sys
from collections import deque
import os

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def int_value():
    return int(input())

def list_ints():
    return list(map(int, input().split()))

def list_strings():
    return list(input())

def string_value():
    return input()

def list_split_strings(c):
    return list(input().split(c))

def map_split_ints():
    return map(int, input().split())

def solve():
    n, l = list_ints()
    lt = list_ints()
    lt.sort()
    mxd = 0
    for i in range(n - 1):
        mxd = max(mxd, (lt[i + 1] - lt[i])/2)
    mxd = max(mxd, lt[0])
    mxd = max(mxd, l - lt[n - 1])
    print(mxd)

if __name__ == "__main__":
    solve()