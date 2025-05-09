import bisect
import sys
from bisect import bisect_left
from collections import defaultdict, Counter
from math import comb, factorial

# Uncomment these lines for local testing
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

    n, t = list_ints()
    s = string_value()
    l = list(s)
    while t > 0:
        t -= 1
        i = n - 2
        while i >= 0:
            if l[i] == 'B' and l[i + 1] == 'G':
                l[i] = 'G'
                l[i + 1] = 'B'
                i -= 1
            i -= 1

    print(''.join(l))

if __name__ == "__main__":
    solve()