import sys
import threading
from math import sqrt

# Uncomment these lines for local testing
#sys.stdin = open('input', 'r')
#sys.stdout = open('output', 'w')

input = lambda: sys.stdin.readline().rstrip()

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
    x, y, z = 0, 0, 0
    for _ in range(n):
        v = list_ints()
        x += v[0]
        y += v[1]
        z += v[2]
    print("YES") if x == 0 and y == 0 and z == 0 else print("NO")

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = int_value() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()