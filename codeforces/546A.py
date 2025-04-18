import sys
import threading

# Uncomment these lines for local testing
#sys.stdin = open('input', 'r')
#sys.stdout = open('output', 'w')

input = lambda: sys.stdin.readline().rstrip()

def int_input():
    return int(input())

def list_int():
    return list(map(int, input().split()))

def string_input():
    return list(input())

def insrsplit(c):
    return list(input().split(c))

def invr():
    return map(int, input().split())

def solve():
    k, n, w = list_int()
    total = 0
    for i in range(1, w  + 1):
        total += i * k
    print(0) if n >= total else print(total - n)

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = int_input() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()