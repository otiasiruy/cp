class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            str_n = str(i)
            n = len(str_n)
            if n % 2 != 0:
                continue
            else:
                str_x1 = str_n[:n//2]
                str_x2 = str_n[n//2:]
                x1, x2 = 0, 0
                for j in str_x1:
                    x1 += int(j)
                for j in str_x2:
                    x2 += int(j)
                if x1 == x2:
                    ans += 1
        return ans