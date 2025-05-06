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
    t = 4 * 60
    sm = 0
    i = 0
    while i < n and sm + k <= t:
        i += 1
        sm += 5 * i

    if sm + k > t:
        i -= 1

    print(i)



if __name__ == "__main__":
    solve()