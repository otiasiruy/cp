import sys
import threading

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

def char_to_int(c):
    return ord(c.lower()) - ord('a')

def solve():
    str1 = insr()
    str2 = insr()
    n = len(str1)
    for i in range(n):
        if str1[i] != str2[i]:
            s1 = char_to_int(str1[i])
            s2 = char_to_int(str2[i])
            if s1 < s2:
                print(-1)
                return
            elif s1 > s2:
                print(1)
                return
    print(0)


def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = inp() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()