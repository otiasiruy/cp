import sys
from collections import Counter

try:
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')
except FileNotFoundError:
    pass

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
    c = Counter(arr)
    l = list(c.values())
    l.sort()
    if len(l) > 2:
        print(l[0] + l[1])
    elif len(l) == 2:
        print(l[0])
    else:
        print(0)


if __name__ == "__main__":
    solve()