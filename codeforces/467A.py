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

    n = int_value()
    cnt = 0
    while n > 0:
        p, q = list_ints()
        if q - p > 1:
            cnt += 1
        n -= 1
    print(cnt)


if __name__ == "__main__":
    solve()