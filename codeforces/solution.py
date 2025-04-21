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
    def is_prime(y):
        if y <= 1:
            return False
        if y == 2 or y == 3:
            return True
        if y % 2 == 0 or y % 3 == 0:
            return False
        i = 5
        while i <= sqrt(y):
            if y % i == 0 or y % (i + 2) == 0:
                return False
            i += 6
        return True

    x, k = list_ints()
    if k > 1 and x > 1:
        print("NO")
    elif k == 1:
        print("YES") if is_prime(x) else print("NO")
    else:
        print("YES") if k == 2 else print("NO")

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = True

    t = int_value() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()