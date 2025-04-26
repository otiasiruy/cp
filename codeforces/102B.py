import sys

# Uncomment these lines for local testing
#sys.stdin = open('input', 'r')
#sys.stdout = open('output', 'w')


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
    if len(s) == 1:
        print(0)
        return
    ans = 1
    n = 0
    for i in s:
        n += int(i)
    while n > 9:
        cnt = 0
        while n != 0:
            cnt += n % 10
            n //= 10
        n = cnt
        ans += 1
    print(ans)


if __name__ == "__main__":
    solve()