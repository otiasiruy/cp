import sys
import threading
from collections import defaultdict, Counter

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

def invr():
    return map(int, input().split())

def solve():
    m = []
    n = 5
    for i in range(n):
        m.append(inlt())

    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                x = i
                y = j
                ans = abs(2 - i) + abs(2 - j)
                print(ans)
                return
    return

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = inp() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()