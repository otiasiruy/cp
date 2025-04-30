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
    arr = list_ints()
    while cnt != 4:
        n += 1
        cnt = len(Counter(str(n)))
    print(n)

if __name__ == "__main__":
    solve()