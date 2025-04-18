class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(n):
            if n == 1:
                return "1"
            s = helper(n - 1)
            count = 1
            c = s[0]
            rle = []
            for i in range(1, len(s)):
                if s[i] != c:
                    rle.append(str(count))
                    rle.append(c)
                    c = s[i]
                    count = 1
                else:
                    count += 1
            if count > 0:
                rle.append(str(count))
                rle.append(c)
            return ''.join(rle)

        ans = helper(n)
        return ans