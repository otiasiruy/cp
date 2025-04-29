import bisect
import sys
from bisect import bisect_left
from collections import defaultdict, Counter
from math import comb

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
    n, h = list_ints()
    f = list_ints()
    cnt = n
    for i in f:
        if i > h:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    solve()