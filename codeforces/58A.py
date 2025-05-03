import bisect
import string
import sys
from bisect import bisect_left
from collections import defaultdict, Counter, deque
from math import comb, factorial

#sys.stdin = open('input', 'r')
#sys.stdout = open('output', 'w')


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
    s = string_value()
    r = "hello"
    n = len(s)
    cnt = 0
    i = 0
    for l in r:
        while i < n and l != s[i]:
            i += 1
        if i > n - 1:
            break
        if l == s[i]:
            cnt += 1
        i += 1
    print("YES" if cnt == len(r) else "NO")

if __name__ == "__main__":
    solve()