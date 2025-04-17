class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = True if num < 0 else False
        if negative:
            num = abs(num)
        base7 = []
        while num != 0:
            base7.append(str(num % 7))
            num = num // 7
        base7.reverse()
        ans = ''.join(base7)
        return "-" + ans if negative else ans