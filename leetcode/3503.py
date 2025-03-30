class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        def generate_substrings(word):
            substrings = []
            substrings.append("")
            for i in range(len(word)):
                for j in range(i, len(word)):
                    substrings.append(word[i:j + 1])
            return substrings

        ans = 1
        sb1 = generate_substrings(s)
        sb2 = generate_substrings(t)
        for i in sb1:
            for j in sb2:
                w = i + j
                n = len(w)
                l = 0
                r = n - 1
                pali = True
                while l < r:
                    if w[l] != w[r]:
                        pali = False
                        break
                    l += 1
                    r -= 1
                if pali:
                    ans = max(ans, n)
        return ans