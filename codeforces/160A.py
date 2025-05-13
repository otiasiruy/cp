import os
import sys

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():

    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    target = sum(a) / 2
    cnt = 0
    sm = 0
    for i in a:
        cnt += 1
        sm += i
        if sm > target:
            print(cnt)
            return
    print(cnt)




if __name__ == "__main__":
    solve()