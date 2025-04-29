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
    n = int_value()
    mx = 0
    cnt = 0
    while n > 0:
        i, o = list_ints()
        cnt += o - i
        mx = max(mx, cnt)
        n -= 1
    print(mx)

if __name__ == "__main__":
    solve()