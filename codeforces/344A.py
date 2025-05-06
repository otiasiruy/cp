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
    t = int_value()
    arr = [int_value()]
    t -= 1
    i = 0
    cnt = 1
    while t > 0:
        t -= 1
        i += 1
        arr.append(int_value())
        if arr[i] != arr[i - 1]:
            cnt += 1
    print(cnt)



if __name__ == "__main__":
    solve()