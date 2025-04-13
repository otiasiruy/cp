import sys
import threading
from collections import Counter, deque

# Uncomment these lines for local testing
#sys.stdin = open('input', 'r')
#sys.stdout = open('output', 'w')

input = lambda: sys.stdin.readline().rstrip()

def inp():
    return int(input())

def inlt():
    return list(map(int, input().split()))

def insr():
    return list(input())

def inpspl():
    return input().split()

def insrsplit(c):
    return list(input().split(c))

def invr():
    return map(int, input().split())

def solve():
    cases = inp()
    for _ in range(cases):
        n, k = inlt()
        arr = inpspl()
        hist = Counter(arr)
        id = -1
        mx = 0
        l = []
        for key, value in hist.items():
            #            print(f"key {key}, value {value}")
            if mx < value:
                mx = value
                id = key
            l.append((value, key))
        #        print(f"id {id}")
        l.sort()
        #        for i in l:
        #            print(f"{i[0]} {i[1]}")
        diff = 0
        for value, key in l:
            if k >= value:
                k -= value
                diff += 1
            else:
                break
        #        for i in arr:
        #            print(f"{i} ", end="")
        #        print()
        if len(l) - diff <= 0:
            print(1)
        else:
            print(len(l) - diff)
def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = inp() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()
