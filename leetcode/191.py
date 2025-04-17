from collections import Counter


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = []
        while n != 0:
            ans.append(n % 2)
            n //= 2
        return Counter(ans)[1]