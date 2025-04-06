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
    n = inp()
    nums = inlt()
    ans = 0
    d = Counter("01032025")
    for i in nums:
        ans += 1
        if str(i) in d:
            if d[str(i)] == 1:
                del d[str(i)]
            else:
                d[str(i)] -= 1
        if len(d) == 0:
            print(ans)
            return

    print(0)

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = True

    t = inp() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()