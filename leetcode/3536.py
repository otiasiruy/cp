class Solution:
    def maxProduct(self, n: int) -> int:
        numbers = list(map(int, list(str(n))))
        numbers.sort(reverse=True)
        return numbers[0] * numbers[1]