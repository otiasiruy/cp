class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w = 0
        b = 0
        n = len(blocks)
        l = 0
        ans = 100
        for i in range(n):
            if b + w == k:
                if blocks[l] == 'W':
                    w -= 1
                else:
                    b -= 1
                l += 1

            if blocks[i] == 'W':
                w += 1
            else:
                b += 1
            if b + w == k:
                ans = min(ans, w)
        return ans