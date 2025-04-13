import sys
import threading
from collections import Counter

# Uncomment these lines for local testing
#sys.stdin = open('input', 'r')
#sys.stdout = open('output', 'w')

input = lambda: sys.stdin.readline().rstrip()

def inp():
    return int(input())

def instr():
    return input()

def inlt():
    return list(map(int, input().split()))

def insr():
    return list(input())

def insrsplit(c):
    return list(input().split(c))

def invr():
    return map(int, input().split())

def solve():
    s = instr()
    ans = ''
    if len(s) > 0:
        ans = s[0].upper()
        if len(s) > 1:
            ans += s[1:]
    print(ans)

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = inp() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()