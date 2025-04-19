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
    s = string_value()
    v = {'a', 'o', 'y', 'e', 'u', 'i'}
    s = s.lower()
    ans = []
    for c in s:
        if c not in v:
            ans.append('.')
            ans.append(c)
    print(''.join(ans))

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = int_value() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()