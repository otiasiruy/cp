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
    tt = sum(arr)
    if tt % 3 != 0:
        print(0)
        return
    target = tt // 3
    ps = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(len(arr) - 1):
        ps += arr[i]
        if ps == 2 * target:
            cnt2 += cnt1
        if ps == target:
            cnt1 += 1
    print(cnt2)

if __name__ == "__main__":
    solve()