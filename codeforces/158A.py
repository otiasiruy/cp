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

def solve():
    n, k = invr()
    nums = inlt()
    ans = 0
    kth = 0
    n = len(nums)
    for i in range(n):
        if i < k - 1 and nums[i] > 0:
            ans += 1
        elif i == k - 1 and nums[i] > 0:
            kth = nums[i]
            ans += 1
        elif i >= k and nums[i] == kth:
            ans += 1
        else:
            break
    print(ans)

def main():
    # Set to True if problem has multiple test cases
    MULTIPLE_TESTS = False

    t = inp() if MULTIPLE_TESTS else 1

    for _ in range(t):
        solve()
if __name__ == "__main__":
    threading.Thread(target=main).start()