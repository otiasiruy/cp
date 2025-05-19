import os
import sys

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    n = int(input())
    x = list(map(int, input().split()))
    mi = min(x)
    ma = max(x)
    ans = float("inf")
    for i in range(mi, ma + 1):
        cnt = 0
        for e in x:
            cnt += (e - i)**2
        ans = min(ans, cnt)
    print(ans)


if __name__ == "__main__":
    solve()