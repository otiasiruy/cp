import sys

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
    n, k = list_ints()
    if n % 2 == 0:
        if k <= n // 2:
            print(2 * (k - 1) + 1)
        else:
            print(2 * (k - (n//2)))
    else:
        if k <= n // 2 + 1:
            print(2 * (k - 1) + 1)
        else:
            print(2 * (k - (n//2 + 1)))

if __name__ == "__main__":
    solve()