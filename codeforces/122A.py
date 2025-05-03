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
    n = int_value()
    def lucky(x):
        for i in str(x):
            if i != '4' and i != '7':
                return False
        return True
    if lucky(n):
        print("YES")
        return
    for i in range(4, n):
        if lucky(i):
            if n % i == 0:
                print("YES")
                return
    print("NO")


if __name__ == "__main__":
    solve()