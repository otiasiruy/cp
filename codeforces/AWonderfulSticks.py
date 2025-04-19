import sys
import threading

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
    n = int_value()
    s = string_value()
    ans = []
    l = 1
    r = n
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '>':
            ans.append(str(r))
            r -= 1
        else:
            ans.append(str(l))
            l += 1
    ans.append(str(l))
    ans.reverse()
    print(' '.join(ans))

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = True

    t = int_value() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()