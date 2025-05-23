import os
import sys

if os.path.exists('../solution/input'):
    sys.stdin = open('../solution/input', 'r')
    sys.stdout = open('../solution/output', 'w')

def solve():
    w = input()
    f_lower = True if w[0].islower() else False
    n = len(w)
    u = 0
    for l in w:
        if l.isupper():
            u += 1
    if u == n or (f_lower and u == n - 1):
        ans = []
        for l in w:
            if l.isupper():
                ans.append(l.lower())
            else:
                ans.append(l.upper())
        print(''.join(ans))
    else:
        print(w)


if __name__ == "__main__":
    solve()