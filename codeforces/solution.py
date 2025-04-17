import sys
import threading

# Uncomment these lines for local testing
#sys.stdin = open('input', 'r')
#sys.stdout = open('output', 'w')

input = lambda: sys.stdin.readline().rstrip()

def int_input():
    return int(input())

def inlt():
    return list(map(int, input().split()))

def string_input():
    return list(input())

def insrsplit(c):
    return list(input().split(c))

def invr():
    return map(int, input().split())

def solve():
    n = int_input()
    arr = string_input()
    repeated = True
    ans = 0
    while repeated:
        found = False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1] and arr[i] != '1':
                arr[i] = '1'
                repeated = True
                found = True
                ans += 1
        if not found:
            repeated = False
    print(ans)



def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = inp() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()