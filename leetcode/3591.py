from math import sqrt
from typing import List


class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        def isprime(x):
            if x <= 1:
                return False
            else:
                for i in range(2, int(sqrt(x)) + 1):
                    if x % i == 0:
                        return False
            return True

        f = Counter(nums)
        for v in f.values():
            if isprime(v):
                return True
        return False