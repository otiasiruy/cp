class Solution:
    def intToRoman(self, num: int) -> str:
        nums = list(map(int, str(num)))
        n = len(nums)
        ans = []
        for i in range(n):
            v = nums[i]
            d = n - i
            it = 0
            if v < 4:
                if d == 1:
                    while it < v:
                        ans.append('I')
                        it += 1
                elif d == 2:
                    while it < v:
                        ans.append('X')
                        it += 1
                elif d == 3:
                    while it < v:
                        ans.append('C')
                        it += 1
                elif d == 4:
                    while it < v:
                        ans.append('M')
                        it += 1
            elif v == 4:
                if d == 1:
                    ans.append('IV')
                elif d == 2:
                    ans.append('XL')
                elif d == 3:
                    ans.append('CD')
            elif v == 5:
                if d == 1:
                    ans.append('V')
                elif d == 2:
                    ans.append('L')
                elif d == 3:
                    ans.append('D')
            if 6 <= v < 9:
                if d == 1:
                    ans.append('V')
                    while it < v - 5:
                        ans.append('I')
                        it += 1
                elif d == 2:
                    ans.append('L')
                    while it < v - 5:
                        ans.append('X')
                        it += 1
                elif d == 3:
                    ans.append('D')
                    while it < v - 5:
                        ans.append('C')
                        it += 1
            elif v == 9:
                if d == 1:
                    ans.append('IX')
                elif d == 2:
                    ans.append('XC')
                elif d == 3:
                    ans.append('CM')

        return ''.join(ans)