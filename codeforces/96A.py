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
    s = string_value()
    seq = 1
    f = s[0]
    for c in s:
        if c == f:
            seq += 1
        else:
            f = c
            seq = 1
        if seq == 7:
            print("YES")
            return
    print("NO")

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = int_value() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()